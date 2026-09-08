#!/bin/bash
# Hook de Notification do Claude Code. Dentro do Maestri, a notificação ativa o Maestri ao clicar;
# fora dele, delega ao hook original do Nori.

NORI_HOOK="/Users/henok/.local/share/fnm/node-versions/v22.22.2/installation/lib/node_modules/nori-skillsets/build/src/cli/features/claude-code/hooks/config/notify-hook.sh"
MAESTRI_BUNDLE="com.evercraftlabs.Maestro"

DATA=$(cat)

if [ "$TERM_PROGRAM" != "Maestri" ]; then
  printf '%s' "$DATA" | "$NORI_HOOK"
  exit 0
fi

MESSAGE=$(printf '%s' "$DATA" | python3 -c 'import sys,json
try: print(json.load(sys.stdin).get("message",""))
except Exception: pass' 2>/dev/null)
[ -z "$MESSAGE" ] && MESSAGE="Claude Code precisa de você"

terminal-notifier \
  -title "Maestri" \
  -subtitle "Claude Code" \
  -message "$MESSAGE" \
  -activate "$MAESTRI_BUNDLE" \
  -group "maestri-$MAESTRI_TERMINAL_ID" \
  -sound default >/dev/null 2>&1

exit 0
