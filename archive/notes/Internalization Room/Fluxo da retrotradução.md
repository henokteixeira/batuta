# Fluxo da retrotradução

O trabalho que começou em 31/08 com os dois defeitos da tela "onde mora o erro" e cresceu para
o fluxo inteiro. **Estado em 04/09, 17:20:** vinte rodadas de teste, **vinte e seis PRs do fluxo abertos e verificados**
(app 13 + servidor 13), todos em inglês no padrão da casa com o id do Linear, todos atualizados com as mains de 04/09
e verdes. Nenhum mergeado por mim. **Um worker vivo: Amparo** (Sonnet), fechando a fatia R19 dentro do #123 (degradar
quando o download da composta falha; lugar pelo id da composta e pelo segmentId; retomada fria sem perder trecho) — em
autorrevisão, ainda não empurrou; quando empurrar, #116 e #125 sobem sobre ela e o app é reconstruído. Servido para
teste: app `44eee66` (sem a fatia Amparo), API `80776a3` (com o áudio composto). **GCS resolvido às 17:45** (conta de serviço `sala-local-signer@`, chave local, assinatura testada com GET 200) — o
download da composta funciona no app servido `44eee66`. **Amparo empurrou `a185bcc` no #123** (721 testes), depois **#125 `b3354db`** (725) e **#116 `6a869aa`** (733, CI verde no rerun, os 3
conflitos de `session_notifier.dart` resolvidos: `_ondeTocar` tenta `_pathForTrecho` — o #116 — e cai no fallback por
`_lugares` — o dela); verifiquei os três no meu worktree (analyze limpo, gate wordless ok, suíte verde). **Colisão nova
(18:20): a main andou de novo — #124 (ENG-609, halts levantados pela Mesa; aviso nunca para a sala) — e mesclada sobre a
cadeia derruba 13 testes** (conserto_que_nao_pegou, o_aviso_nao_fecha_o_azul, onde_mora_o_erro, retro_untold_stretch:
"esperado invite, veio needsPerson"). Medido com carga baixa: **10** reprovam, não 13 — 9 são só a vigia nova do
halt deixando Timer pendente (6 em `onde_mora_o_erro_test`, 3 em `retro_untold_stretch_test`; mesmo conserto que o #124
fez nos testes dele) e **1 é regra contra regra**: `o_aviso_nao_fecha_o_azul_test.dart:177` (#112) diz que o toque longo
derruba o aviso de um conserto recusado; o #124 diz que só a Mesa levanta um halt confirmado. Assumi que o #124 vence
(é do Henok, de hoje) e registrei na *Tasks*. **Rollup com o #124 (Amparo, 18:40–19:50):** 11 de 12 branches empurradas e verificadas por mim (todas carregam a
main; além do diff do próprio #124 só mudaram testes: `closeTheRoom` no fim dos 9 casos parados e o caso do #112 reescrito
para a regra nova); #116 novo `0102e18` = 744 verdes, analyze limpo, gate ok. CI verde nas 10 primeiras. O #101
trouxe mais 3 do mesmo tipo em `conserto_que_nao_pegou_test` (2 timers + 1 regra: a recusa na substituição) — mesma
decisão aplicada, verificado (`e22a1b5`, só testes; "sem pedir para repetir" continua afirmado). Fecha a conta dos 13. **App servido reconstruído sem o #124** (composto local `daaeda6` = #116 + #113 +
#101, 736 testes) — a fatia Amparo está nele. Ordem de merge e o que depende de você: *Tasks for Henok*.

**SHAs finais (19:50, sobre a main com o #124).** App: #100 `d96c088` · #96 `040b442` · #111 `3c49b89` · #112 `e8ba9da` ·
#113 `68bdd56` · #115 `f3653dd` · #117 `bc352f0` · #121 `4b25ad3` · #123 `ef7adc0` · #125 `d6c2bf6` · #116 `0102e18` · #101 `e22a1b5`. Doze carregam a main de hoje (`e381a21`, #124); CI verde nas doze.
**App servido (05/09, 14:10): composto local `9ee9d00`** (= #126 + #113 + #101, 750 verdes). Relatório publicado:
https://claude.ai/code/artifact/fbbdb010-f2df-4cb6-9ee2-a82b901819d5 API: #303 `458deb2` ·
#305 `1af37c0` · #309 `606fd1f` · #316 `8559b84` · #315 `51de0c0` · #318 `cd03029` · #326 `622a715` · #317 `8881ace` ·
#323 `a6d6d89` · #327 `fc2eb0e` · #334 `3e27c95` · #310 `77f9789` · #312 `9a37d80`.

## 07/09, 23:00 — a API está na main; o fluxo inteiro fechou

Com a mão do Henok no `--admin` (o bot só comenta), os 13 PRs da API entraram na ordem: #303 `391aca3` · #305 `619f288` ·
#309 `720e4b9` · #315 `babe615` · #317 `27fc929` · #316 `1fb6229` · #318 `6fd490f` · #326 `b037e0c` · #323 `ffa0f17` ·
#327 `ba406d7` · #334 `c8bd498` · #310 `f4533f0` · #312 `c90b88c`. Dois rollups antes disso: com o #336 (Prumo, 05/09) e,
depois de o meu primeiro laço não parar na falha do #316 e deixar #315/#317 entrarem antes, com a main parcial (Prumo,
07/09). Cada merge disparou um deploy no Cloud Run. #295 e #296 fechados (dentro do #303). Cartógrafo avisado. Linear:
todas as issues do fluxo em Done.

## 05/09, 13:55 — o app está na main

Com autorização do Henok ("somente dessa vez"), os 13 PRs do app foram mergeados na ordem, um por vez, cada um
retargetado para a main e conferido `MERGEABLE CLEAN` antes: #100 `a5ab2d9` · #96 `97ba0b3` · #111 `c4c3684` · #112
`1c903b8` · #113 `9ab223a` · #115 `d22624c` · #117 `acc5017` · #121 `eb60acb` · #123 `053c5f7` · #125 `fea6094` · #116
`63cb165` · #126 `554054c` · #101 `adc7981`. #110 e #114 fechados sem merge. Linear fechou sozinho ENG-721, 724, 742 e
824; ENG-705, 706, 710 e 720 ficam abertas até a metade da API entrar. A API espera o rollup com o #336 (Prumo).
Relatório: https://claude.ai/code/artifact/fbbdb010-f2df-4cb6-9ee2-a82b901819d5

## Rodada de 05/09 (banco zerado, app reinstalado, composto `2ef3dd9` sobre a main com o #124)

- [ ] **Rollup da API com o #336 (ENG-609)** — medido às 13:20: a main da API (`d124485e`) tem 10 commits que a cadeia não
      carrega e o topo (#334) conflita em `app/api/internalization_room/back_translation.py` e
      `app/services/internalization_room/__init__.py`. Plano `~/.maestri/handoff/rollup-336/plano.md`; **Prumo** (Opus,
      worktree `~/.maestri/worktrees/shema-api/rollup-336`) despachado. Regra: os dois lados sobrevivem; contradição de
      intenção para e reporta.

- [x] **Áudios conferidos fora do app** (perícope 1, 6 partes, correções nos trechos 3 e 4 pelo caminho longo e 6 pelo
      curto): 19 takes baixados de `gs://tripod-platform` para `~/.maestri/handoff/audios/P01-2026-09-05/`, nomeados pelo
      que são; as compostas das partes 3 e 4 têm a duração exata da regravação (cada parte virou um trecho só — sem
      costura visível nesta gravação). O usuário conferiu: "contou tudo correto".
- [ ] **R21 · o play da tela do ensaio pulou a parte 2** (não corrigida; arquivo local de 11,5 s existe; take `4e652584`
      intacto no servidor). Partes 1, 3 (composta), 4 (composta), 5 e 6 tocaram. O app não imprime log; `em_curso.json`
      já estava vazio (perícope fechada). **Medido:** `ghostPlay` → `_tocarTrechoFantasma` resolve cada trecho por
      `_pathForTrecho` (id do take em `keptTakes`, sem fallback) e pula em silêncio quando vem `null`; a retro usa
      `_ondeTocar`, que cai no lugar guardado. O gatilho do id que não casa ainda não foi provado. **ENG-824** aberta;
      **PR #126** (`7332740`, sobre o #116): `ghostPlay` passa a resolver por `_ondeTocar`, que ganhou um terceiro
      nível (a parte no lugar do trecho, `lugarFrom..lugarTo`); 3 casos novos, um reprova no pai (composta que não baixou
      some do play). Verificado: 747 verdes, analyze, gate, RED no pai. **O gatilho do caso real não foi reproduzido** (o
      caso base com os dois downloads ok passa antes do conserto); Amparo sondando a variação "nome da parte 2 chega
      tarde". Plano `~/.maestri/handoff/play-do-ensaio/plano.md`.

## Pacote de 03/09 — "quando eu voltar, quero só mergir tudo" (em medição → planos → workers)

Decisões do usuário no fim do teste: **corrigir tudo neste pacote**, atualizar as listas. Frentes:
- [ ] **R13 · play vira pause — PR #115** (sobre o #112), diff lido: estados pausada/tocando por voz, 2º toque
      pausa (`_holdClip`), 3º retoma da posição, ícone segue o estado, e o **teto** que desligava o estado agora
      **para o player de verdade** (hipótese do "recomeça" confirmada pelo caso 5). 621 testes, CI verde, verificado.
- [ ] **R11 · calibração do analista — PR #326**, verde nos cinco, verificado. Seção "Wording varies. Content does
      not." no prompt do analista, com o incidente de hoje como exemplo trabalhado ("felizes"/"novo marido").
      Sonda nos 10 transcritos reais: antes 3/3 `addition`; depois 0/3; sem cegar (sem a bênção → `missing` 3/3;
      Boaz de fora → `addition` 3/3). **Texto do prompt para sua revisão no corpo do PR.** Edge registrado lá:
      "nome no lugar de descrição" pode colidir com `preservation_violation` num mapa que retém nome de propósito.
- [ ] **R9 · a volta ao ensaio diz, em voz, o que fazer.** O app tem gate no CI "The room stays wordless" (a
      equipe não lê; texto na tela é proibido) — Letreiro parou no gate em vez de contornar; o #114 fecha sem
      merge. A instrução vai para o fechamento falado do servidor (`CLOSING_MISSING_TO_REHEARSAL` nomeia o microfone
      grande e o botão verde). **PR #327** (sobre o #323), verde nos cinco, verificado — só o texto do bloco e dois
      testes. Texto para sua revisão no corpo do PR.
- [ ] **R10 · falta dentro do trecho passa a oferecer os dois microfones.** App: **PR #113**, verde, verificado
      (o `if` sai; `RefazerAParte` removido; reversível = reintroduzir o `if`). **O #110 fica superado** — conflita
      com o #113; comentei lá; não mergear, fechar. Servidor: **PR #323**, verde nos cinco, verificado (falta com
      endereço fecha com `CLOSING_ON_SCREEN`; bloco de um microfone removido; testes da ENG-676 de volta às duas vozes).
- [ ] **R19 (04/09, 19:20) · o download do take composto deu 500 e a sala parou por uma pessoa.** Visto ao vivo no teste do
      zero: `room_listens_to_take` → `generate_signed_download_url` → `'Credentials' object has no attribute
      'service_account_email'` — o "signing-key" local é credencial de usuário (403 bytes), não conta de serviço; assinatura
      de URL nunca funcionou aqui e ninguém baixava takes antes do #123. Dois consertos: a chave (Henok, na *Tasks*) e o app
      degradar em vez de parar (**fatia Amparo**, dentro do #123). **Consequência vista ao vivo (16:23):** na retomada
      fria o trecho 3 (corrigido, no servidor apontando para a composta `cbb1d73f`) sumiu do colar e a sala mandou contar
      a parte 3 de novo — o app não tem a composta (download 500) e o `lugares` do `em_curso.json` só conhece a materna
      antiga (`6946a428`). Amparo estendida: lugar registrado também pelo id da composta e pelo segmentId; trecho com
      lugar mas sem arquivo conta como contado (colar, chão, sem recontar) e toca o melhor áudio local (materna própria /
      fatia antiga da parte); a composta entra quando o download voltar a funcionar. **Aberto, sem explicação:** às 19:17:28 e 19:18:48 o corte do
      trecho 4 falhou duas vezes (áudio foi para a fila `passagem-inteira`) e a sala parou por uma pessoa — sem traceback,
      **medido:** o pedido nunca saiu do tablet — em `_finishChunkCapture` a parte "no ar" não tinha id
      (`_aGravacaoNoAr` nulo) embora o servidor já tivesse a parte 4 há 38 s; o app enfileirou o áudio como emergência e
      chamou de `RoomBroke` → parou por uma pessoa. Defeito do app na volta ao ensaio (adoção do id / índice da parte).
      **R20 — PR #125** (sobre o #123, ENG-721): raiz medida na fila — `TakeUploadQueue.flush()` concorrente virava no-op
      silencioso e `_adoptTheName` só tentava uma vez; agora o flush espera e repassa, e um corte antes do nome não é
      `RoomBroke` (a sala fica viva). Reenviar o corte guardado quando o nome chegar ficou FORA: é a decisão da ENG-721.
      719 testes; CI verde. **Verificado.**
- [ ] **R17 (04/09, 14:25) · sessão retomada desloca os trechos uma casa.** Medido no banco (P04 `5c241b86…`,
      gravada 02/09, retomada hoje): depois de o trecho 1 ter sido corrigido pelo caminho longo, a retomada criou os
      ordinais 2–5 sobre os takes dos ordinais **anteriores** (2 ← take do antigo 1, 3 ← do antigo 2, 4/5 ← do
      antigo 3). Cada trecho retomado foi contado sobre o áudio do anterior — daí o analista dizer que o fim veio
      antes. **Raiz:** o trecho corrigido guarda só (take próprio, 0..27 s); na retomada `_trechosFrom` não acha esse take
      entre as partes → `parte = −1` → o chão contado da parte 1 vira zero → a sala recomeça a parte 1 e cada corte novo
      herda o take da parte anterior. E o colar desenha 27 s num lugar de 6 s. O trecho precisa de **lugar** (parte +
      intervalo original) separado de **o que toca**, persistido no resume. **PR #121** (sobre o #117), verde: `Trecho`
      ganha `lugarFrom/lugarTo`; colar, chão contado e próximo corte leem o lugar; `_tocarOTrecho` lê o que toca; o
      lugar vai ao `em_curso.json`. Rollup com #116 + #113 + main: 55 verdes nas famílias juntas e **699 na suíte
      inteira**; lints do analisador novo consertados (`5b022d6`, CI verde). **Verificado.**
- [ ] **R18 (04/09) · a correção deve gerar um áudio NOVO da passagem** (o original com o trecho errado cortado e o
      corrigido no lugar), não só tocar o take certo por trecho (#116). Pedido reiterado do dono do produto; vale
      para o app e para os fluxos seguintes. **Medido:** takes são arquivos inteiros no GCS (m4a); `ffmpeg` já está na
      imagem e há precedente de subprocesso (`split_service.py`); o modelo de segmento é fatia de UM arquivo por desenho.
      Composição no `replace`: take novo da passagem (original com o trecho cortado + corrigido no lugar), todos os
      segmentos daquele take reapontados com inícios/fins recalculados; falha na composição não bloqueia (cai no #116).
      **PR #334** (`feat(ir): the mend becomes the passage audio (ENG-705)`, sobre o #327), verde nos cinco, verificado:
      `compose_passage` (ffmpeg atrim/asetpts/aformat/concat, re-encode AAC), `recompose_passage` reendereça todos os
      segmentos do take (e filhos de trecho dividido), a resposta do `replace` traz `composed_take_id`; ffmpeg real
      medido no host e no container (8,000 s ± 0,1). Enxerto deixou nomeada a **armadilha da caixa de saída**: uma
      ponte enfileirada antes da remontagem drena apontando para o arquivo velho — medido no app: **não existe fila
      de chunks offline** (o `sendChunk` é ao vivo; em falha o áudio cai na fila de takes inteiros), a armadilha não se
      aplica. **Metade do app — fatia Cola** (Opus, `fix/sala-the-composed-passage-becomes-the-part`, sobre o #121):
      **PR #123** (`feat(sala): the composed passage becomes the part (ENG-705)`, sobre o #121): lê `composed_take_id`,
      baixa o take composto (`fetchClip` pelo 307), troca a parte no lugar (mesmo `scopeId`, `KeptScope.composed`),
      pontes dos vizinhos por `segmentId`, resume frio mapeia o composto pelo `chunk_index` da listagem de takes
      (sem listagem, não troca nada — teste próprio). 12 casos, 645 na suíte, mutações. **Rollup com #116 + main:** analyze limpo, famílias juntas 43 verdes, suíte 710 verdes e
      **1 vermelho da main** (#120: todo pedido do `RoomRepository` apresenta a credencial do tablet e consta da tabela do
      `device_credential_test`; o `takesOf` novo ficou fora) — Cola mesclou a main e acrescentou as linhas (`c665e42`,
      provado por mutação). **Rollup final: 713 verdes, analyze limpo** (árvore `44eee66`); CI verde. **Verificado.**
      Não verificado ao vivo: o 307 da URL assinada com o header X-Room-Key (precisa da API com o #334 servida).
- [ ] **R15 (03/09, 15:05) · o player do take do ensaio não pausa nem muda o ícone** (o play branco depois de
      gravar, `takePlay`) — toca do zero a cada toque, ícone fixo; o `ghostPlay` ao lado já faz o certo.
- [ ] **R16 (03/09, 15:05) · a esfera laranja, num achado, repete a pergunta.** A fala do achado é o turno do
      narrador, já guardada em `lastSpoken` com `hearAgain()` pronto — só não estava ligado à esfera (que tocava
      o trecho). Decisão: esfera = repetir a fala; os players da grade continuam com o trecho.
      **PR #117** (sobre o #115), verde, verificado: `takePlay` pausa/retoma (`takePaused`), ícone segue o estado; a
      esfera em `findings` repete a última fala do narrador (`_repeatTheFinding`; o veredito passa a ser lembrado
      salvo fail-safe); 628 testes.
- [ ] **R14 · a correção tem de ocupar o áudio (ENG-705, reaberta).** "Quando eu regravo um trecho, a nova gravação
      deve substituir a errada; quando voltei, ele me pôs no áudio errado de novo." Eu tinha fechado a ENG-705
      na terça como "promessa já cumprida" — errado para quem ouve. **Medido:** o take corrigido da materna nunca
      entra em `keptTakes`/`partes`; a reprodução resolve o arquivo por índice (`partes[parte]`), e o #111, ao herdar
      `parte` para o colar, fez tocar o **take original** no intervalo da correção; ao retomar, `parte` = −1 e o
      toque cala. Servidor certo (Refine recebe o corrigido). Fatia **Voz** (Opus, `fix/sala-the-mend-is-the-audio-now`,
      sobre o #112): lugar (colar) e arquivo (por `takeId`, em `keptTakes`) separados. **PR #116**, diff lido:
      `_pathForTrecho` resolve por `takeId`; o take corrigido entra em `keptTakes` com escopo `trecho-…` e
      sobrevive ao resume; `partes` exclui os de trecho (colar estável); e o **ouvir a passagem** do ensaio
      (`ghostPlay`) passou a percorrer os trechos com o arquivo corrigido. CI verde (1º run caiu no instável
      conhecido do ensaio, rerun verde). **Verificado.**
- [x] Rótulos de acessibilidade da grade no ensaio: é o cross-fade de 400 ms do `AnimatedSwitcher` — não é defeito.
- [ ] Player da ponte desabilitado uma vez na grade de falta — sem evidência além do instante; fica de olho.

**04/09, 17:20 — segunda reconciliação da API com a main** (#313, #329–#333). Conflito de intenção novo em
`run_turn.py` (TEAM_UTTERANCE do brief do validador): o #303 distingue "nunca falou" de "contou de volta" só em pt; a main
traduz a abertura por idioma sem distinguir. **Decidido: unir** — dicionário por idioma com os dois casos, fallback da
main. Costura2 aplicando de baixo para cima (primeiro lote sem `ruff format --check` — vermelho; consertando na base e
reaplicando). **App: as onze branches com a main, CI verde nas onze (Alinha, dispensada).**

**Servido às 12:40:** API em `db47031` = cadeia inteira do fluxo (#303, #305, #309, #316, #315, #318, #326, #317,
#323, #327) — **sem a main nova**. A main da API andou oito PRs da outra equipe (#311…#325; #320 muda como os prompts
são carregados) e **as dez branches do fluxo conflitam com ela** (só #310 e #312 limpas). Emenda está
reconciliando de baixo para cima (#303, #305 → #309 → #316 → #315 → #318 → #326; #317 → #323 → #327).
**14:55:** um conflito de intenção apareceu e foi decidido — a main (#320) fez `get_prompt_text` síncrona e só de
arquivo (a tabela `ir_prompts` nunca teve linha nem chamador); a cadeia inteira foi portada para isso. As dez
saem limpas contra a main atual; suíte inteira verde nos topos (#326: 2547; #327: 2553). Resta o grafo do
alembic: a junção `20260903_join5` nasceu nos topos e falta nas de baixo (`migrations` vermelho de #303 a #318)
— e a junção era o remédio errado: a nossa `20260901_room09` só acrescentava um valor ao enum de `ir_prompts`, que
a main (`20260902_room09`) apagou inteira; nunca entrou na main, logo nunca rodou em produção. **Decidido:** apagar a
901 e as junções em toda a cadeia; ponta única = a da main. **Feito (18:10):** as dez reconciliadas, limpas contra
a main, ponta única `20260902_room09`; **CI verde nos cinco nas dez** (22:20). SHAs:
#303 `5c7f815` · #305 `c3f967a` · #309 `b14a55e` · #316 `95a4a03` · #315 `c0c6fd4` · #318 `b9c6115` · #326 `5a74a0a` ·
#317 `ca13c41` · #323 `6c5c06c` · #327 `2fedf6c`.
**API servida:** ainda `db47031` (cadeia antiga, com a 901) — a árvore reconciliada (`52838ba`) não sobe aqui porque o
banco local está carimbado na 901 apagada, e recarimbar o banco é escrita que o classificador me bloqueia. Comando
para o Henok rodar (banco de teste, não produção); depois eu troco a árvore e reinicio:
`! docker exec tripod_db psql -U $(docker exec tripod_db env | grep ^POSTGRES_USER= | cut -d= -f2) -d $(docker exec tripod_db env | grep ^POSTGRES_DB= | cut -d= -f2) -c "update alembic_version set version_num='20260831_lang01'"` App remontado às 22:30 em `091c2c9` (main + cadeia até o #117 + #113 + #116 + #101), instalado e sob o portal;
31 verdes nos cinco arquivos das fatias juntos (a árvore anterior, sem o #117, tinha 635 verdes na suíte inteira).

**Workers (03/09, 11:15):** Batida (Sonnet, R13 play/pause), Timbre (Sonnet, R14/ENG-705), Fala (Sonnet, R9
falado), Medida (Sonnet, R11 calibração + sonda). Opus caiu em 529 por uma hora — Pulso e Voz trocados por
Sonnet nos mesmos worktrees. Dobra (#113), Vozes (#323) e Letreiro (#114 fechado) dispensados. Planos em `~/.maestri/handoff/{play-pausa,
ensaio-instrucao,falta-dois-mics,analista-calibra,falta-duas-vozes}/plano.md`. App sobre o #112; servidor sobre o #318.

## Rodada de 02/09 à noite — dois achados sobre a pilha da tarde (fechada às 21:40; em teste)

- [ ] **R9 (03/09, 09:53) · a tela de volta ao ensaio não se explica.** O usuário contou parte da história,
      a sala disse que faltava e mandou seguir — e ele não entendeu os botões (tocar, microfone grande, quatro
      bolinhas, verde de concluir). Nada diz "grave o resto e toque no verde". Print em
      `~/.maestri/handoff/logs/prints/`. A árvore de acessibilidade no mesmo instante trouxe rótulos da grade
      de correção — conferir se os rótulos estão desencontrados. **Conversar com ele depois do teste; não agir.**

- [ ] **R10 (03/09, ~10:00) · falta dentro do trecho: um botão só, materna+ponte.** Tela `RefazerAParte`
      (dois players, um microfone "Regravar esta parte e contá-la de novo"). É a decisão de 02/09 à noite
      (falta no meio → contar a parte inteira de novo), não bug — mas o usuário reabriu a pergunta: **falta
      de conteúdo exige regravar a materna, ou bastaria recontar só a ponte?** (Leitura real do momento:
      `missing, chunk 5, where: inside` — a bênção "descanso na casa de seu marido"; o `where` do #316 em uso.)
      Decisão de produto; conversar
      depois do teste. No mesmo instante o player "Ouvir o contar em português" estava **desabilitado** —
      conferir se era só "algo tocando" ou o R3 de volta. Print em `prints/`.

- [ ] **R11 (03/09, ~10:05) · `addition` possivelmente falso:** analista devolveu `addition, chunk 5` — "o relato
      acrescenta que Noemi desejou que as noras fossem 'felizes'". Provável paráfrase de "encontrar
      descanso na casa do marido" (Rt 1:9) lida como acréscimo. **Padrão, não caso isolado:** em seguida
      `addition` por "os maridos seriam 'novos'" e de novo por "a palavra 'novo' em 'novo marido'" — três
      adições por um adjetivo, no mesmo trecho, com a verificação do conserto entre elas voltando limpa
      (`carried` 5/5 ainda ditos, `brought_back` vazio — o #315 como desenhado). Calibração do analista
      para adição: um adjetivo/paráfrase não é acréscimo; só o que muda o que a história conta. Só anotado.

- [ ] **R12 (03/09) · o analista oscilou no mesmo trecho, 4–5 correções.** Sequência real do log (#318):
      leitura 1 = `meaning_change` ch.3 + quatro `missing` ch.4 `where: after` → **ensaio** (o #316 e o caso B
      funcionando; foi a tela do R9). Depois, no trecho 5: `addition` "felizes" → o usuário tira → `missing`
      "descanso na casa do marido" → põe de volta → `addition` "novo marido" → tira → `addition` "felizes" de
      novo → … até fechar. O analista trata adjetivo/paráfrase como acréscimo e o mesmo conteúdo como falta,
      alternando. É o R11 medido: calibração de `addition` (e de `missing` no limite da paráfrase). Custou
      4–5 regravações de um trecho certo. **Caso de borda relatado pelo usuário:** um achado de falta citou
      algo já dito no trecho anterior (candidato: leitura 2, `missing` ch.1 "Noemi se levantou para sair de
      Moabe", ou leitura 5); ele não repetiu e o achado não voltou. Família do endereço na fronteira.
- [x] **Visto em uso real (03/09, 10:07, P02):** o turno conferido do #317 — "…essa parte está conferida. Esta
      passagem está contada e verificada." — sem pergunta, sem "como se sentem"; a tela voltou ao seletor de
      passagens. O `carried`/`brought_back` do #315 voltou limpo nas duas verificações. Print `conferida.png`.

**PRs da noite, todos verdes nos cinco checks:** app **#112** (o aviso não fecha o azul); servidor **#315**
consertado (`brought_back`), **#316** reconciliado com o #305 (`2742af9`), **#318** (toda leitura deixa
rastro; `88b0358`). Zero workers vivos.

- [ ] **R7 · fail-safe A que "nunca deve acontecer"** (P06, 21:12 UTC). Medido no banco: não foi o analista
      nem o narrador — o **verificador de correção** devolveu um `addition` falso ("ficar com as servas não
      está na história", quando o Mapa diz isso na Proposição 1); o narrador obedeceu; o validador pegou
      (`invented_absence`) duas vezes → "Vamos com calma". Repetiu na recontagem seguinte. O servidor não
      guarda leituras aceitas, então não dá para saber se o prompt novo do #315 causou. Fatia **Sonda**
      (`henok/every-reading-leaves-a-trace`, **PR #318**): registra toda leitura aceita (INFO, com sessão).
      **Sonda decisiva:** o `addition` falso vem **só do prompt do #315** (3/3 novo, 0/3 antigo): a contagem
      `carried` é da contagem anterior, e o modelo passou a ler "não estava na anterior" como "o Mapa não
      conta". Conserto em curso DENTRO do #315: a regra 'Added' passa a dizer que o que o Mapa dá nunca é
      adição, mesmo que a anterior não o tivesse. **A frase sozinha não bastou** (3/3 ainda): o modelo não
      revisita o Mapa depois de contar. Conserto estrutural que fechou: lista `brought_back` (o que a
      contagem nova trouxe do Mapa e a anterior não tinha) + cinto mecânico no parser (um `addition` com as
      palavras de um `brought_back` é suprimido). Sonda: P06 **0/3**, Rute 1 sepultamento **3/3**. Commit
      `4d089e7` no #315. O #318 (rastro) conflita com o #316 no mesmo módulo — Sonda reconciliando.

**Build de teste às 21:20:** app `2b61bdd` (+ #112); API = checkout principal em `ebc73ea` (#318, que carrega
#309 + #315 consertado + #316 + #305, mais #317 e main) — ruff limpo, 114 verdes nos sete arquivos do fluxo.
Sonda achou no caminho um vazamento de merge textual: o import auto-mesclado trocou `UpstreamServiceError`
por `UnreadableReply` e deixou dois usos órfãos (F821) — consertado no #318 e no #316 (`2742af9`); cinco
checks verdes nos dois. O container **monta o checkout como
volume** com `--reload` — trocar a pilha é mudar o checkout e `docker restart`, sem `--build`.
- [ ] **R8 · "o mic azul não funciona"**: o banco tem duas gravações com transcrição **vazia** (21:14:50 e
      21:17:03), cada uma seguida de regravação que funcionou; nenhum turno falado nas vazias — a sala se
      calou. **Medido, e eu li errado:** as vazias são o passo intermediário do caminho longo (a materna
      regravada cria um segmento ainda sem contagem) — a equipe foi pelo caminho longo porque o azul não
      respondeu. Causa real: `retells=4` → o servidor manda `needs_person` (aviso, PR #310) e o app trata
      como teto só no azul: `contarDeNovo` engole o toque em silêncio (`if (state.needsPerson) return`);
      o longo não tem guarda. Metade do app da **ENG-706**. **PR #112**, verde, verificado (guarda
      `needsPerson` sai do azul; offline continua fechando, agora com o botão visivelmente inerte).
- Portal de dispositivo **"Sala"** aberto sobre o simulador (app sob o portal, árvore de acessibilidade).
  Log do app agora em `~/.maestri/handoff/logs/flutter-run.log` (o de rascunho sumiu com a sessão).

## Rodada de 02/09 à tarde — "deve ser a última" (seis fatias verdes; em teste desde 18:05)

**Build de teste:** app `3b2347e` = main + #100 + #96 + #101 + #110 + #111; API `9011230` = main + #303 +
#305 + #309 + #315 + #316 + #317. Os arquivos de teste das fatias irmãs rodaram juntos sobre cada árvore
integrada (117 verdes na API, 54 no app). `ir_prompts` local está vazia — os prompts novos valem no teste.

**Ordem de merge da API agora:** `#303` e `#305` (irmãs) → `#309` → `#315`, `#316`, `#317` (irmãs, sobre o
#309) · `#310`, `#312` independentes. **App:** `#100` → `#96` → `#111` · `#101`, `#110` (irmãs sobre o #100).
**Dependência nova:** o #305 (ENG-719) conflita com o #316 (`_session_of` e o estilo de recusa) — Sonda está
mesclando o #305 dentro do #316 e depois o #316 no #318, para que a ordem de merge fique linear: `#303` →
`#305` → `#309` → `#316` → `#315` → `#318`, com `#317` irmão.

Seis achados do teste das 15:50, Rute 1:15-18, cinco trechos gravados e um faltando no fim:

- [ ] **R1** · faixa do colar esvazia ao escolher o caminho longo (materna+ponte); no caminho curto
      (só ponte) o trecho continua cheio. Cheiro: id novo do conserto, antes de a gravação existir.
- [ ] **R2** · `missing` no último trecho: dois players e UM microfone **azul** que percorre os dois
      caminhos. Decidir: botão único com o visual do caminho longo (âmbar com o azul pequeno embaixo),
      ou os dois botões de volta.
- [ ] **R3** · player da língua-ponte esmaecido na grade de correção — depois de a sala pedir uma
      pessoa (R3a) e numa correção comum após consertos (R3b). Só dá para ouvir a materna.
- [ ] **R4** · redundância do analista: corrigido o trecho 4, ele voltou ao 3 dizendo que o conteúdo
      do 4 novo não tinha sido dito; o mesmo conteúdo acabou em 3 e em 4. Servidor.
- [ ] **R5** · ao terminar, a sala perguntou "como vocês estão se sentindo" e encerrou. Não precisava.
- [x] **R6** · no geral, "bem melhor" — sem achado.

**Medido (16:30):** R1 e R3 são a mesma família — o caminho longo cunha um `takeId` novo e a tela deriva
`parte`/`retroPath` por casamento com a identidade antiga; e nenhuma correção grava o `retroPath` novo
(só a primeira contagem). R2 é lacuna visual (`RefazerAParte` não reusa o visual do caminho longo). R4
é uma **cascata** vista no banco: a falta do v.18 (depois de tudo) foi apontada ao chunk 5 em vez de ir ao
ensaio → a equipe substituiu o 5 e perdeu o juramento → recontou o 4 e perdeu o sepultamento (a
`verify_correction` pede o "perdido" mas o modelo não o vê: cegueira de omissão, arXiv 2608.31016) →
a releitura apontou o sepultamento ao chunk 3. R5 é texto livre sob "termine com uma pergunta" no turno
em que não há próximo turno.

**Seis fatias no ar (sobre #100 no app, sobre #309 no servidor):**
| | fatia | worker |
|---|---|---|
| R1+R3 | o conserto guarda o lugar e a voz — **PR #111**, verde, verificado (mutação separa as duas metades; achado extra: posição lida depois da resposta, corrigido) | Lugar · Opus (dispensado) |
| R2 | o botão único mostra as duas estações — **PR #110**, verde, verificado | Pendura · Sonnet (dispensada) |
| R4 | a verificação enumera o que o trecho carregava — **PR #315**, diff lido, sonda no par real: antes nenhum `missing`, depois o sepultamento como não dito; CI verde nos cinco | Zelo · Opus (dispensado) |
| R4 | a falta diz onde fica: `where: before/inside/after` — **PR #316**, verde, verificado; sonda nos transcritos originais: antes `chunk:5`, depois `chunk:5, where:after` → ensaio | Rumo · Sonnet (dispensado) |
| R5 | o turno conferido não pergunta — **PR #317**, verde nos cinco, verificado; achado extra corrigido dentro: a linha fixa "they will finish the telling-back again" saiu do .md e mora só nos blocos com próximo turno | Selo · Sonnet (dispensada) |

Decidido sem você (reversível): a ponte antiga NÃO sobrevive à materna nova (teste existente vence o caso
4 do plano); o botão único de falta ganha o visual do caminho longo em vez de virar dois botões.

## Esperando você — depois das suas decisões de 02/09 de manhã

- [ ] **Uma fala que virou instrução ao narrador, para você revisar na PR.** A fala do caso B
  não era uma linha fixa: era o bloco de fechamento prometendo um próximo turno de conversa que
  não existe. Reescrevi os dois blocos (falta com e sem endereço) como instrução ao narrador —
  a língua entra por substituição, então não há três versões. Estão na branch
  `henok/the-closings-match-the-screen`.
- [ ] **Uma frase no prompt do analista**, na mesma branch, para que `null` seja só para o que
  vem depois do fim e uma falta do meio nunca vá ao ensaio. É prompt de agente, e você revisou
  os anteriores — revise esta.
- [ ] **O que a sala oferece para adição, mudança de sentido e violação SEM endereço.** Único
  ponto aberto da ENG-720: hoje o microfone azul preservador é a única saída, e gravar mais não
  corrige uma adição. Destacado no topo do PR #100.
- [ ] **ENG-721** · esperar o upload do ensaio antes de deixar cortar, ou guardar o corte e
  subir depois? Equipe rápida em rede lenta perde trechos em silêncio.
- [ ] **ENG-723** · ao retomar no ensaio sem o áudio no tablet: pedir restart, ou ir direto à
  retro?
- [ ] **Os dois prompts de produção** dos PRs #294 e #295.
- [ ] Confirmar o âmbar do círculo (já no build) e o rótulo `Contar esta parte na língua ponte`.
- [ ] Modo de Desenvolvedor no iPhone — só você alcança.

## Decidido em 02/09 de manhã, e o que virou

- [x] **ENG-705** · é promessa, e já se cumpre: o caminho longo faz o trecho apontar para a
  gravação nova. Fechada sem código.
- [x] **ENG-706** · é aviso, não teto. **PR #310**, verde, verificado: só nome e documentação, nenhum `if` tocado; um teste de guarda (a rota aceita além da marca). Achado fora do escopo registrado no PR: `test_the_retells_are_counted_and_run_out` reimplementa o `if` dentro do teste.
- [x] **ENG-710, metade falada** · não será feita — custo e complexidade da máquina de estados.
- [x] **ENG-720, refinamento** · ensaio só quando a falta está depois do último trecho; a
  distinção mora no endereço do analista, e o prompt ganha a frase que a garante.

## O que você decidiu na madrugada, e virou trabalho

**Achado de falta tem dois casos, distinguidos pelo endereço:**
- **Com endereço** (a falta cabe num trecho existente) → fluxo do "onde mora o erro", com **um
  botão só, o do caminho longo** (regravar materna e contar). *"Somente o botão que tem o mic
  da língua materna e o da tradução, senão fica confuso."* → ajuste dentro do **#94**.
- **Sem endereço** (a falta está além do último trecho) → volta ao ensaio **mantendo tomadas,
  trechos e colar**, grava mais, e ao avançar **só os trechos novos** são contados. → **ENG-720**,
  fatia nova. Você provou que o caminho de retomada já preserva tudo: saiu e reentrou na
  passagem, e estava tudo lá. É o botão azul que destrói — e destrói no servidor também: os cinco
  segmentos da sua sessão P04 ficaram aposentados.

**A faixa do colar esvazia no segundo passo do caminho longo** — enche ao regravar a materna,
esvazia ao passar para contar. → dentro do **#91**.

## Nenhum worker meu ativo. Tudo o que foi despachado fechou.

O que sobrou está registrado e espera decisão sua — nada está parado por falta de mão.

## O que a madrugada fechou

| frente | quem | onde |
| --- | --- | --- |
| ENG-720 · falta o fim da história, sem apagar | worker novo | branch própria, de `origin/main` |
| ENG-710 · botão único vira caminho longo | autor do #94 | dentro do #94 |
| ENG-707 · a faixa pelo caminho longo | autor do #91 | dentro do #91 |
| ENG-719 · o parser guarda o que consegue ler | **PR #305**, cinco portões verdes, 2.371 testes | na API de teste, carregado no processo |
| ENG-720 · falta o fim da história, sem apagar | **PR #100**, verde, reconciliando com a corrente | 562 testes verdes na pilha sem ele; entra assim que o README fechar |
| ENG-723 · retomar no ensaio sem áudio no tablet | registrada, não despachada | último buraco da família da retomada; decisão sua entre restart e ir direto à retro |
| ENG-724 · conserto que não pega devolve à reprodução, calado | **PR #101**, verde, na pilha | é o que você viu como "a faixa tirou"; a faixa estava certa, a sala se calou. Conserto sem fala nova: volta à pergunta e diz a linha de repetir que já existe |
| ENG-721 · equipe rápida em rede lenta perde trechos em silêncio | registrada, **decisão sua** | a raiz dos testes instáveis era de produção: corte antes do upload terminar é descartado |
| a suíte espera pelo que quer dizer | **PR #96**, verde, só testes | a raiz era uma só: os testes entravam na retro antes de a sala nomear a gravação, e um corte sem nome é **descartado** — ver abaixo |

## O build de teste, como ficou às 5h de 02/09

**App:** `main + #100 + #96 + #101` — o #100 virou o topo da corrente e carrega #87, #83, #84, #89,
#90, #94 e #91. **590 testes, zero falhas, zero instáveis.** Treze correções dentro, no simulador.
**API:** `main + #303 + #305` — o #303 carrega as cinco fatias do servidor; o #305 é a ENG-719.
Conferido dentro do processo: família I da frase e `UnreadableReply` carregados.

**Ordem de merge agora é simples:** app `#100`, depois `#96`, depois `#101`; servidor `#303` depois `#305`.
Os PRs intermediários entram por dentro deles. O PR dos **fechamentos é o #309** (`2fe822b`, CI verde,
MERGEABLE), sobre o #303 porque precisa do slot do validador da ENG-676. Fecho reconciliou os três
(#303, #305, #309) com a main que andou cinco PRs da outra equipe (#302–#308). Dentro do #309, além
dos dois blocos: a frase do analista (falta antes do primeiro trecho → chunk 1; `null` só para
depois de tudo), os dois testes da ENG-676 atualizados para um microfone, o suplemento do fail-safe
PT/ES corrigido (família I dizia 'dois microfones'), e — em curso — a **pergunta de fronteira sai**
para missing nos dois casos (ela decidia substituir vs. acrescentar; essa escolha não existe mais).

**Build de teste às 12:45 de 02/09:** API `main + #303 + #305 + #309 final` (`4b96754`, pergunta de fronteira removida); app
`main (com #109) + #100 + #101 + #96` (`1322a7c`). O token do gcloud expirou às 11h e a
reconstrução derrubou a API por ~10 min; regra nova: conferir o token antes de qualquer `up`.

**Colisão da manhã de 02/09:** a equipe do backlog mergeou o **#108** (ENG-708), um ajudante de espera
para a suíte inteira. O **#96** fazia a mesma coisa com outro arquivo — duas equipes, mesma ideia, mesma
noite, sem se ver. Decidido: o #108 vence porque já está na main; o #96 encolhe para o que é só dele
(as conversões que o #108 não fez, na linguagem do #108, e a raiz da ENG-721). Se ficar vazio, fecha
sem merge. **Fechado às 11:14:** o #96 (`2a5c9b9`) ficou com as seis conversões originais mais cinco
da mesma forma que o árbitro sob carga 45–75 derrubou; seis rodadas verdes. App de teste em
`main + #100 + #101 + #96`.

**Dívida da suíte, fora do fluxo (sugestão, não plano):** ainda há 12 testes told-back com 5 a 10
esperas fixas em `session_notifier_test.dart`, o helper `_intoConferida` (4 fixas, uma de 900ms),
e dois fora da retro que caíram uma vez sob carga (`the back-translation reaches conferida and
closes the necklace`, `a take that ran out of tries is said out loud, once`). Mesma raiz da
ENG-721. É trabalho da suíte inteira — cabe à equipe do backlog (dona do #108), não a esta corrente.

## As correções — nenhuma mergeada além das quatro visuais

Na **main**: #80 grade · #82 botão de corte · #88 bolinha · #89 faixa enche ao começar.
Abertos: #83 (681) · #84 (686) · #87 (694, **topo da corrente**, carrega 83/84/90) · #90 (692 app) ·
#91 (707) · #94 (710).
Servidor: #294 (676) → #295 (679) → #296 (680) · #297 (685) · #299 (692) · **#303 (693, topo da
corrente, carrega os cinco)**.

**Ordem de merge não é livre:** app `#83 → #89 → #90 → #84 → #87`, e `#94` e `#91` depois do #87;
servidor `#299` antes do `#90`, e `#303` por último.

## O que a madrugada descobriu, e ainda está aberto

- **ENG-719** · o analista responde JSON válido com achados válidos e o parser joga tudo fora
  em silêncio por uma contradição entre o flag geral e um achado específico; a rota chama isso
  de "falha do serviço externo". Capturei a resposta crua rodando o analista dentro do container.
  A regra escolhida: o achado específico vence o flag — uma passagem que o próprio analista
  disse estar incompleta não é dada por conferida. Em conserto.
- **O fail-safe da família A** da noite de 01/09 continua sem explicação. Provavelmente a mesma
  classe da ENG-719 — o servidor não registra o que o validador recusou. A ENG-719 põe log em
  todas as saídas do parser do analista; o do validador ainda não tem.
- **ENG-721 · confirmado de produção, não de teste:** uma equipe rápida numa rede lenta perde os dois primeiros trechos da retrotradução em silêncio. O corte antes de o upload do ensaio terminar é descartado (`_finishChunkCapture`), a tela não impede (`startRetro` não exige nome), e a sala volta ao repouso calada — só na terceira falha pede pessoa. **Precisa de decisão sua:** a tesoura espera o upload, ou o corte fica guardado e sobe depois? Não despachada.
- **Feito, PR #312** (irmã da ENG-719, sem issue nova; comentado na ENG-719): o validador deixa rastro de cada recusa — condição, sessão, tentativa e a resposta bruta do validador; nunca o rascunho do guia (política do teste `without_repeating_what_the_team_said`). Os dois silêncios (JSON sem `verdict`; rejeições por tentativa) acabaram. CI verde, 2387 testes. Achado fora do escopo no PR: `bridge_language.strays_from` registra 120 caracteres do rascunho num outro logger. Foi a primeira fatia feita por um worker Sonnet — limpa. Da próxima vez que a família A disparar, o log diz por quê. (Texto antigo: fatia própria, pequena, a despachar assim que a 719 fechar.
- **A máquina chegou a `load average` 262 com 12 núcleos.** Toda medição local é suspeita; o CI
  também, porque os testes esperam por tempo fixo. O árbitro é o teste isolado, repetido.

## O ambiente de teste

**API** — compose no diretório principal, **SEMPRE com os dois `-f`**. Um `up -d` sem o override
recria o container sem o projeto do GCP, ele continua "saudável", e o erro só aparece quando a
sala busca áudio ("Project was not passed"). Já me pegou duas vezes:

```
cd /Users/henok/Documents/programming/obt/shema-api
docker compose -p shema-api -f docker-compose.yml \
  -f ~/.maestri/handoff/compose-projeto-gcp.yml up -d
```

Se a sala travar por dois minutos sem erro, é DNS: cada falha de resolução leva 120s.
Se o container morrer no arranque com "Can't locate revision", o banco tem uma migração que a
árvore não tem — a branch de teste perdeu uma fatia.

**App** — worktree `/Users/henok/.maestri/worktrees/internalization-room/testar`, `.env` próprio
em `localhost:8000`. `flutter run -d <simulador>` em debug, com barra de fases.