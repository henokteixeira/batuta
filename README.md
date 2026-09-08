# batuta

A vara do maestro. Este repositório guarda o fluxo de trabalho do Henok com agentes no Maestri: o skillset, os papéis dos terminais, os scripts e os templates. Serve para qualquer projeto, não só para a Shema.

## O que há aqui

- `skillset/` — skillset Nori `personal/batuta`: o CLAUDE.md global (`AGENTS.md`), as skills (núcleo Nori de execução mais as skills de definição do Matt Pocock) e os subagentes. Ligado ao Nori com `nori-skillsets link`.
- `roles/` — os três papéis do Maestri. O preset no app é só um ponteiro para o arquivo; a verdade mora aqui.
  - `definidor.md` — conversa com o Henok, grelha, escreve glossário e ADR, publica specs e tickets definidos no Linear.
  - `orquestrador.md` — puxa tickets `ready-for-agent`, escreve o plano de fatia, recruta executores, verifica contra spec e testes. Nunca edita repositório.
  - `executor.md` — um plano, um worktree, TDD com falsificação manual, PR. Morre com a PR.
- `bin/notify-maestri.sh` — hook de Notification do Claude Code que abre o Maestri ao clicar, em vez do Terminal.
- `templates/` — conteúdo inicial das notas do canvas e o texto dos presets.
- `docs/fluxo.md` — como o fluxo funciona, do ticket ao merge.
- `arquivo/notas/` — as notas dos workspaces antigos, exportadas em 08/09/2026, para migrar o que for decisão para ADR e glossário.

## Como o fluxo se divide

Definição antes do despacho. O Definidor fecha regra de negócio, critério de aceitação e decisões com o Henok, em lote. O Orquestrador só recebe o que está rotulado `ready-for-agent`, fatia em planos com Testing Plan intocável, e despacha executores com modelo e effort escolhidos por ticket. O executor grelha só decisões de implementação, espera em vez de supor, e entrega PR com evidência. A verificação é contra a spec, não só contra os testes.

Os detalhes estão em `docs/fluxo.md` e nos papéis.

## Instalar numa máquina nova

```
git clone git@github.com:henokteixeira/batuta.git ~/Documents/programming/batuta
nori-skillsets link ~/Documents/programming/batuta/skillset --name personal/batuta
nori-skillsets switch personal/batuta
```

Depois, no Maestri: criar os três papéis com o texto de `templates/presets.md`, e apontar o hook de Notification do `~/.claude/settings.json` para `bin/notify-maestri.sh`.
