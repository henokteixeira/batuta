#!/bin/bash
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/bin"
cat > "$T/bin/maestri" <<'EOF'
#!/bin/bash
D="$(cd "$(dirname "$0")/.." && pwd)"
{ for a in "$@"; do printf '%s ⟨ ' "${a//$'\n'/ }"; done; echo; } >> "$D/calls.log"
case "$1 ${2:-}" in
  "list ") cat "$D/list.txt" ;;
  "routine list") cat "$D/routines.txt" ;;
esac
EOF
chmod +x "$T/bin/maestri"
export PATH="$T/bin:$PATH"

failed=0
check() { if [ "$2" = "$3" ]; then echo "ok    $1"; else echo "FAIL  $1: expected '$3', got '$2'"; failed=1; fi; }
calls() { grep -c -E -- "$1" "$T/calls.log"; }
line() { grep -c -F -x -- "$1" "$T/calls.log"; }
flat() { printf '%s' "$(cat "$1")" | tr '\n' ' '; }
run() {
  : > "$T/calls.log"
  printf '%s\n' "$1" > "$T/list.txt"
  printf '%s\n' "$2" > "$T/routines.txt"
  bash "$ROOT/bin/setup-canvas" > "$T/out.txt" 2>&1
  echo $?
}

MAESTRO='You:
  - name: "Orquestrador", maestro: true
Connected agents:
  - name: "Definidor"'
NOTES='Notes:
  - name: "board"
  - name: "for you"
  - name: "findings"
  - name: "how it works"
  - name: "round"
  - name: "voice"'
OLD='Notes:
  - name: "painel"
  - name: "pra você"
  - name: "achados"
  - name: "como funciona"'

echo "# fresh workspace cloned from an old one"
rc=$(run "$MAESTRO
$OLD" "")
check "exits 0" "$rc" 0
for n in painel "pra você" achados "como funciona"; do
  check "deletes old note '$n'" "$(line "note ⟨ delete ⟨ $n ⟨ ")" 1
done
for n in board "for you" findings "how it works" round; do
  check "creates note '$n' from its template" "$(line "note ⟨ create ⟨ $(flat "$ROOT/templates/notes/$n.md") ⟨ --name ⟨ $n ⟨ ")" 1
  check "wires '$n' to the Definer" "$(line "connect ⟨ $n ⟨ Definidor ⟨ ")" 1
done
check "recruits the voice terminal" "$(calls "^recruit ⟨ voice ⟨ ")" 1
check "wires voice to the Definer" "$(line "connect ⟨ voice ⟨ Definidor ⟨ ")" 1
for r in "morning state" "evening round check" "for you reminder"; do
  check "creates routine '$r'" "$(calls "^routine ⟨ create ⟨ $r ⟨ ")" 1
done
check "edits no routine" "$(calls "^routine ⟨ edit ⟨ ")" 0

echo "# populated workspace with the old evening routine name"
rc=$(run "$MAESTRO
$NOTES" "morning state
evening handoff
for you reminder")
check "exits 0" "$rc" 0
check "creates no note" "$(calls "^note ⟨ create ⟨ ")" 0
check "deletes no note" "$(calls "^note ⟨ delete ⟨ ")" 0
check "rewrites 'how it works' from its template" "$(line "note ⟨ write ⟨ how it works ⟨ $(flat "$ROOT/templates/notes/how it works.md") ⟨ ")" 1
check "rewrites nothing else" "$(calls "^note ⟨ write ⟨ ")" 1
check "creates no routine" "$(calls "^routine ⟨ create ⟨ ")" 0
check "refreshes 'morning state'" "$(calls "^routine ⟨ edit ⟨ morning state ⟨ --command ⟨ ")" 1
check "renames and refreshes 'evening handoff'" "$(calls "^routine ⟨ edit ⟨ evening handoff ⟨ --name ⟨ evening round check ⟨ --command ⟨ ")" 1
check "refreshes 'for you reminder'" "$(calls "^routine ⟨ edit ⟨ for you reminder ⟨ --command ⟨ ")" 1

echo "# populated workspace with the current routine names"
run "$MAESTRO
$NOTES" "morning state
evening round check
for you reminder" >/dev/null
check "refreshes 'evening round check' in place" "$(calls "^routine ⟨ edit ⟨ evening round check ⟨ --command ⟨ ")" 1
check "renames nothing" "$(calls "^routine ⟨ edit ⟨ .*--name ⟨ ")" 0

echo "# terminal without Maestro Mode"
rc=$(run 'You:
  - name: "Claude Code", maestro: false' "")
check "exits 1" "$rc" 1
check "only lists, touches nothing" "$(wc -l < "$T/calls.log" | tr -d ' ')" 1

if [ "$failed" = 0 ]; then echo "all green"; else echo "red"; exit 1; fi
