# Como funciona o fluxo Batuta

Escrito na madrugada de 08/09/2026, na noite em que o fluxo foi montado. Leia isto antes de abrir o canvas.

## Em uma frase

Definir antes de despachar: você e o Definidor fecham a regra de negócio e as decisões em lote; o Orquestrador só recebe tickets prontos e os leva até PRs verificadas por executores descartáveis; ninguém supõe, todo mundo pergunta e espera.

## O canvas

Um workspace só para a Shema, chamado **Shema**, raiz em `~/Documents/programming/obt`. Nele:

- **Definidor** — o terminal com quem você conversa para definir. Fable, effort alto.
- **Orquestrador** — o terminal que executa a fila. Fable, effort alto ao planejar. Precisa de **Maestro Mode ligado** para recrutar executores: ligue no botão do terminal na primeira vez.
- **Claude Code** — um terminal solto, sem papel, que veio da clonagem. Pode apagar ou usar como shell.
- Quatro notas: **painel** (uma linha por tarefa em curso), **pra você** (só o que está travado esperando você; perguntas fechadas), **achados** (o que apareceu fora do escopo; só cresce), e o fichário **logs** (estado de cada rodada e log de cada tarefa; você quase nunca abre).

Os workspaces antigos estão na pasta **Arquivo** dentro do grupo Shema YWAM, intactos, com os terminais e as notas. Apague quando quiser; as notas já estão exportadas em `batuta/arquivo/notas/`. O workspace **teste** na pasta "Arquivo (apagar)" foi o molde e pode ser apagado. O **Quick Sermon** não foi tocado.

## Uma rodada, do começo ao fim

1. **Definir.** Abra o Definidor e traga a lista: tickets, defeitos vistos num teste, ideias, linhas `Definir:` que o Orquestrador deixou em `pra você`. Ele grelha item a item, uma fronteira por rodada, cada pergunta com a resposta recomendada. Fatos ele busca; a você vão só decisões. Ele atualiza o glossário (`CONTEXT.md`) e escreve ADRs conforme conversa, publica spec e tickets no Linear com bloqueios, e só põe `ready-for-agent` no que está inteiro: regra em uma frase, critério de aceitação como teste que falha, zero decisões pendentes.
2. **Despachar.** Diga ao Orquestrador para começar a rodada. Ele lista os tickets `ready-for-agent` sem bloqueio, escreve o plano de fatia em `~/.maestri/handoff/<branch>/plano.md` com o Testing Plan intocável e os caminhos enumerados, cria o worktree, recruta um executor com o modelo e o effort do ticket, e despacha. No máximo três tarefas em curso e uma grelhando você por vez.
3. **Responder.** Você só olha `pra você`. Cada linha é uma pergunta fechada ou uma aprovação de alto risco. Responda ali, ditando pelo Whispr Flow. Quando responde, a linha some.
4. **Verificar.** O executor entrega PR com evidência: suíte colada, falsificação de cada teste, o que fez fora do plano. O Orquestrador lê o diff, roda tudo, passa o revisor nos dois eixos (padrões e fidelidade à spec), espera a CI, e só então avança o painel. Mudança visível você olha no portal ou simulador.
5. **Fechar.** Decisões vão como comentário no ticket. Achados viram ticket ou são descartados. O executor é reiniciado. No fim, o Orquestrador escreve `estado · <data>` no fichário logs e termina com TASK_COMPLETE ou BLOCKED.

A rodada seguinte começa num Orquestrador reiniciado lendo essa nota. As notas são a memória; a sessão não é.

## Modo de alta autonomia

Só quando você pedir. O Definidor fecha a fila inteira primeiro; quando nada resta a definir, ele escreve `modo: alta autonomia` na primeira linha do painel. O Orquestrador então dispara toda a fronteira de uma vez, sem o limite de três. Ao encerrar a rodada, apaga a linha. Nunca é padrão.

## Modelos

Decisão e estudo no mais forte: Definidor e Orquestrador em Fable, effort alto. Implementação no mais barato que o ticket permite: 1 ou 2 e risco baixo, sonnet com effort baixo; 3, sonnet com effort alto; 5, risco alto ou regra de domínio, opus com effort alto. Revisor de fidelidade em opus. Haiku nunca.

## Onde mora cada coisa

- `~/Documents/programming/batuta` — este repositório: skillset, papéis, scripts, templates. GitHub privado em `henokteixeira/batuta`.
- `~/.claude/CLAUDE.md` — gerado pelo Nori a partir de `batuta/skillset/AGENTS.md`. Skillset ativo: `personal/batuta`.
- Papéis no Maestri (`Definidor`, `Orquestrador`, `Executor`) — só ponteiros para `batuta/roles/*.md`. Edite o arquivo, não o preset.
- Linear, time Engineering — rótulos novos `ready-for-agent` e `ready-for-human`. Seis tickets de organização de documentação dos repositórios já criados, um por repo.
- `CONTEXT.md` do internalization-room e do shema-api — em PR, para você revisar.

## O que mudou no Nori

Skillset `personal/batuta` no lugar do `public/high-autonomy`. Saíram brainstorming, root-cause-tracing, creating-debug-tests-and-iterating, webapp-testing, building-ui-ux, ui-ux-experimentation, creating-a-skillset, updating-noridocs e os subagentes de documentação e de padrões. Entraram grilling, grill-me, grill-with-docs, domain-modeling, to-spec, to-tickets, code-review, handoff, wizard, to-questionnaire e wayfinder. As seis skills do Maestri e a de limpeza do Mac agora fazem parte do skillset, para não sumirem numa troca.

## Notificação

O hook de Notification do Claude Code aponta para `batuta/bin/notify-maestri.sh`: dentro do Maestri, clicar na notificação abre o Maestri; fora dele, cai no hook do Nori.
