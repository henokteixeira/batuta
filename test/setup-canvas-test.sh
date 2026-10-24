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
  - name: "for you"
  - name: "findings"
  - name: "round"'
OLD='Notes:
  - name: "painel"
  - name: "pra você"
  - name: "achados"
  - name: "como funciona"
  - name: "board"
  - name: "how it works"'

echo "# fresh workspace cloned from an old one"
rc=$(run "$MAESTRO
$OLD" "")
check "exits 0" "$rc" 0
for n in painel "pra você" achados "como funciona" board "how it works"; do
  check "deletes old note '$n'" "$(line "note ⟨ delete ⟨ $n ⟨ ")" 1
done
for n in "for you" findings round; do
  check "creates note '$n' from its template" "$(line "note ⟨ create ⟨ $(flat "$ROOT/templates/notes/$n.md") ⟨ --name ⟨ $n ⟨ ")" 1
  check "wires '$n' to the Definer" "$(line "connect ⟨ $n ⟨ Definidor ⟨ ")" 1
done
check "recruits no terminal" "$(calls "^recruit ⟨ ")" 0
check "wires nothing but the three notes" "$(calls "^connect ⟨ ")" 3
check "creates no routine" "$(calls "^routine ⟨ create ⟨ ")" 0

echo "# populated workspace with the old routines and a leftover voice terminal"
rc=$(run "$MAESTRO
  - name: \"voice\"
$NOTES" "morning state
evening handoff
evening round check
for you reminder")
check "exits 0" "$rc" 0
check "creates no note" "$(calls "^note ⟨ create ⟨ ")" 0
check "deletes no live note" "$(calls "^note ⟨ delete ⟨ ")" 0
check "overwrites no note" "$(calls "^note ⟨ write ⟨ ")" 0
check "leaves a leftover voice terminal alone" "$(calls "^connect ⟨ voice ⟨ ")" 0
for r in "morning state" "evening handoff" "evening round check" "for you reminder"; do
  check "deletes old routine '$r'" "$(line "routine ⟨ delete ⟨ $r ⟨ ")" 1
done
check "creates or edits no routine" "$(calls "^routine ⟨ (create|edit) ⟨ ")" 0

echo "# workspace with a routine of Henok's whose name contains an old one"
run "$MAESTRO
$NOTES" "morning state digest" >/dev/null
check "keeps a routine that only contains an old name" "$(calls "^routine ⟨ delete ⟨ ")" 0

echo "# terminal without Maestro Mode"
rc=$(run 'You:
  - name: "Claude Code", maestro: false' "")
check "exits 1" "$rc" 1
check "only lists, touches nothing" "$(wc -l < "$T/calls.log" | tr -d ' ')" 1

if [ "$failed" = 0 ]; then echo "all green"; else echo "red"; exit 1; fi
