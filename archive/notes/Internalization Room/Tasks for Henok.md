# Tasks for Henok

Só ponteiros. O detalhe está na nota **Fluxo da retrotradução** (atualizada 07/09, 23:10).

**Estado: o fluxo inteiro está na main dos dois repositórios.** API de teste servida na main (`c90b88c`), banco na
ponta `20260904_att01`; GCS assinando com a conta `sala-local-signer@`. Cartógrafo avisado (ENG-666/665 destravadas).

## App (`internalization-room`) — mergeado
- [x] **13 PRs mergeados na main em 05/09, 13:53–13:55, com a sua autorização (só desta vez), na ordem:** #100 `a5ab2d9` ·
      #96 `97ba0b3` · #111 `c4c3684` · #112 `1c903b8` · #113 `9ab223a` · #115 `d22624c` · #117 `acc5017` · #121 `eb60acb` ·
      #123 `053c5f7` · #125 `fea6094` · #116 `63cb165` · #126 `554054c` · #101 `adc7981`. #110 e #114 fechados sem merge.
      Linear fechou ENG-721, 724, 742, 824; ENG-705, 706, 710, 720 seguem abertas até a API. CI da main: verde (`adc7981`).

## API (`shema-api`) — mergeada
- [x] **13 PRs na main em 07/09, na ordem, com a sua mão no `--admin`:** #303 `391aca3` · #305 `619f288` · #309 `720e4b9` ·
      #315 `babe615` · #317 `27fc929` · #316 `1fb6229` · #318 `6fd490f` · #326 `b037e0c` · #323 `ffa0f17` · #327 `ba406d7` ·
      #334 `c8bd498` · #310 `f4533f0` · #312 `c90b88c`. #295 e #296 fechados (já estavam dentro do #303). Cada merge
      disparou o deploy no Cloud Run. Linear: ENG-693, 705, 706, 710, 719, 720, 743, 744, 745, 746 fechadas.
- [ ] **Prosa do orçamento de recontos:** a main diz que o `needs_person` do orçamento "para a sala"; o #310 diz "aviso,
      não teto". Os testes concordam; só o texto discorda. Uma PR de texto sua, quando quiser.

## (histórico) Mergear — API
- [ ] **Prontos, verdes nos cinco, limpos contra a main** (reconciliados em 03/09; decisões embutidas: a
      `get_prompt_text` da main vence — só arquivo; a nossa migração `20260901_room09` foi apagada, nunca rodou em
      produção). Ordem: `#303` (ENG-693) e `#305` (ENG-719) → `#309` (ENG-710/720) → `#316` (ENG-720) → `#315`
      (ENG-744) → `#318` (ENG-719) → `#326` (ENG-743); `#317` (ENG-745) → `#323` (ENG-710) → `#327` (ENG-746); `#310`
      (ENG-706) e `#312` (ENG-719) soltos; e **`#334` (ENG-705, o áudio composto) depois do `#327`**. **07/09: mergeados na main #303 `391aca3`, #305 `619f288`, #309 `720e4b9`, #315 `babe615`, #317 `27fc929`.** O laço
      que eu te passei não parava na primeira falha (erro meu): #316 não entrou e #315/#317 entraram antes dele, e agora
      #316, #318, #326 e #323 conflitam com a main. Prumo está reconciliando os 8 restantes
      (`~/.maestri/handoff/rollup-336/plano-2.md`). **07/09, 19:20: as 8 restantes estão limpas contra a main e verdes (#310 com um check fechando). Laço novo
      entregue no chat; ele para na primeira falha.** Prosa para você depois: a main diz que o `needs_person` do orçamento
      "para a sala", o #310 diz "aviso"; testes concordam, só o texto discorda. Estado anterior:
      atualizadas com a main de 04/09 (#313, #329–#333), CI verde nas treze. Decisão
      embutida nova: no brief do validador, "nunca falou" × "contou de volta" (nosso) e idioma (main) foram unidos.
      Cada dia de PRs abertos custa uma passada dessas. Issues novas de 04/09 para os achados do teste que
      não eram correção de issue existente: ENG-742, 743, 744, 745, 746 (projeto, milestone, você, estimativa, relações). **Atenção:** a main da API anda todo dia; se ao mergear algum
      conflitar de novo, me chame antes de resolver à mão.
- [x] ~~Recarimbar o banco de teste~~ — feito em 04/09 (`alembic stamp 20260831_lang01`, com a sua autorização). A API
      reconciliada, com o áudio composto (#334), sobe aqui assim que Costura2 fechar #323 → #327 → #334.

## Textos para sua revisão (estão nos corpos dos PRs)
- [ ] Fechamentos do narrador: `#309`, `#317` (turno conferido), `#323` (falta com endereço = duas vozes),
      `#327` (volta ao ensaio nomeia o microfone grande e o botão verde).
- [ ] Prompt do analista: `#316` (`where`) e `#326` (calibração "wording varies, content does not", com o
      incidente "felizes / novo marido" como exemplo).
- [ ] Prompt do verificador de correção: `#315` (`carried` + `brought_back`, sondas 3×3).
- [ ] Prompts de produção `#294`, `#295` (da rodada de 01/09).

## Para o áudio composto funcionar neste servidor de teste
- [x] ~~Uma chave de conta de serviço do GCS~~ — **feito às 17:45, com você:** conta nova `sala-local-signer@` (`objectViewer` +
      `objectCreator` nos DOIS buckets que a API usa — `tripod-image-uploads` e `tripod-platform`, o do cache de falas do
      narrador, concedido em 05/09 depois de a sala ficar muda por falta dele — e `Token Creator` nela mesma), chave em `shema-api/gcs-signing-key.json`
      (600, ignorada pelo git), API reiniciada, assinatura testada de dentro do container (GET 200). A credencial de
      usuário antiga está em `~/.maestri/handoff/gcs-user-credential-2026-09-01.bak`, fora do repositório — apague quando
      quiser. **Pendências suas:** (1) apagar essa chave quando o teste local acabar (`gcloud iam service-accounts keys
      list --iam-account=sala-local-signer@gen-lang-client-0886209230.iam.gserviceaccount.com`); (2) o bucket
      `tripod-image-uploads` tem `allUsers` como `objectViewer` — qualquer pessoa com o caminho lê o áudio das equipes sem
      URL assinada; decida se isso é intencional. Produção usa a conta padrão do Cloud Run e assina sem chave, não
      precisa de nada.

## Relatório
- [ ] **Relatório pedido (05/09):** https://claude.ai/code/artifact/fbbdb010-f2df-4cb6-9ee2-a82b901819d5 — o que mudou no
      servidor e no tablet, sobre os dois documentos-base; ordem de merge e ressalvas no fim.

## Decisões embutidas que você pode reverter
- [ ] **A regra do #124 venceu dois testes antigos (mergeado):** um conserto recusado que chama uma pessoa só é levantado
      pela Mesa; o toque longo pede releitura (casos reescritos em #112 e #101). Reverter = um `if` em `resolveWithPerson`.
- [ ] **R10:** falta dentro do trecho voltou a ter os dois microfones (você esperava poder escolher só a
      ponte). Reverter = reintroduzir um `if` (#113) e um ramo de `closing_block` (#323).
- [ ] **R3-janela:** entre regravar a materna e recontar a ponte, a ponte antiga NÃO fica audível (o teste
      `caminho_longo_test.dart:101` diz que ela "não vale mais"). Mantive.
- [ ] **ENG-720 sem endereço** para adição/mudança de sentido/violação; **ENG-721** (esperar o upload ou guardar
      o corte — hoje, com o #125, um corte antes do nome vai para a fila de emergência e a sala fica viva, mas ninguém
      reenvia esse corte: decida se o app reenvia sozinho quando o nome chega); **ENG-723** (restart ou retro ao retomar
      sem áudio). Nenhuma trava o teste.

## Miúdas
- [ ] Modo de Desenvolvedor no iPhone. → *Fluxo*.
- [x] ~~Conferir `ir_prompts` em produção~~ — caiu com o #320 da main (prompts vêm só dos arquivos).

Decididas e feitas: ENG-705 (reaberta 03/09; conserto no #116), ENG-706 (aviso, não teto — servidor #310, app
#112), ENG-710 metade falada (não será feita), ENG-720 refinamento (falta do meio nunca vai ao ensaio).

## Do backlog da Sala (Cartógrafo) — rodada fechada 04/09 17h30

Relatório: https://claude.ai/code/artifact/203342fc-4f9f-4e16-af85-1c19bd9deaac · detalhe na nota *Backlog da Sala*.
Nenhum worker vivo. 37 PRs mergeados, 33 issues Done.

- [x] ~~ENG-741 · aprovar o Keychain~~ — aprovado 07/09; em curso com o worker Estojo.
- [x] ~~Revisão linguística en/es da Mesa (#79)~~ — você aprovou os textos como estão em 07/09 (as ENG-683/682 do João continuam com ele).
- [x] ~~Autorizar os merges~~ — #127 e #128 mergeados por mim 08/09 com o seu "pode mergear"; o #129 (Keychain) fecha a última emenda e então pede a mesma palavra → *Backlog da Sala*, topo.
- [ ] Review plan for ENG-792 fatia A (API) — proceeding on: `POST/DELETE /facilitator/devices/{id}/attended` (escopo pelo projeto do tablet; marcar levanta a parada e carimba; desfazer devolve a parada com o momento original só se foi esta marca que a levantou); `POST /sessions/{id}/person-arrived` carimba o primeiro toque por parada e a Mesa lê na fila e no histórico; quatro colunas, uma migração. Fatias B (Mesa: botão na linha do tablet, frase de quem tocou) e C (app: o toque longo chama person-arrived antes da releitura) despachadas em paralelo contra este contrato; planos b-the-desk.plan.md e c-the-app.plan.md na mesma pasta. Plano: ~/.maestri/handoff/eng-792/a-the-api.plan.md
- [ ] **ENG-595 · App Store** — só suas contas.
- [x] ~~Mergear a corrente do app~~ — feito 05/09; ENG-666/665 destravadas e em curso (07/09).
- [x] ~~Review plan for ENG-666/665~~ — aprovado 07/09; proceeding on: a parte retomada começa a tocar no cursor (`initialPosition` no `just_audio`, posição absoluta no arquivo; sem clip); o que foi ouvido conta a partir do cursor; a guarda da tesoura fica como cinto; a 665 fecha por um teste que enumera todo jeito de a reprodução nascer atrás do cursor — se sobrar um, a frase falada volta como pergunta sua. Plano: ~/.maestri/handoff/eng-666/the-resumed-retelling-starts-at-the-cursor.plan.md
- [x] ~~Review plan for ENG-790~~ — aprovado 07/09; proceeding on: um booleano `warning` no estado, que segue a última leitura do servidor (estado `halt: warning` ou `needs_person` do chunk da retro); o círculo do facilitador desenha o disco verde que o `done` já usa quando há aviso e a voz não está parada; nada falado, nenhum gesto muda. Plano: ~/.maestri/handoff/eng-790/the-facilitator-circle-turns-green-on-a-warning.plan.md
