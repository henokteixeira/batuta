# Backlog da Sala

Nota do Cartógrafo, fechada em 04/09 às 17h30. Relatório completo da rodada:
https://claude.ai/code/artifact/203342fc-4f9f-4e16-af85-1c19bd9deaac
(cópia em ~/.maestri/handoff/relatorio/relatorio-final-04-09.html; histórico detalhado em feito-ate-03-09.md).

---

# ⬛ O QUE DEPENDE DE VOCÊ

- [ ] **#341 (API) · ENG-792 fatia A — pronto, verificado por mim; seu merge, primeiro da ordem.** Rotas
  `POST/DELETE /facilitator/devices/{id}/attended` (escopo pelo projeto do tablet; marcar levanta a parada e carimba;
  desfazer devolve a parada com o momento original só se foi esta marca que a levantou; um halt novo limpa os
  carimbos da visita anterior, como nas sessões) e `POST /sessions/{id}/person-arrived` (primeiro toque por parada,
  servido na fila e no histórico). Duas migrações (uma por tabela, o walk de `devices` exige), uma ponta. Verificado:
  2649 verdes na suíte, 19 nos arquivos novos, 7 vermelhos contra a main, mypy limpo. Bot "nothing else from me" no
  SHA final de7efb94; job de testes do CI fechando. Ressalva registrada no PR: person-arrived aceita qualquer tablet
  da instalação (mesma janela das rotas irmãs). https://github.com/shemaobt/shema-api/pull/341
- [ ] **#81 (Mesa) · ENG-792 fatia B — pronto na minha verificação, CI rodando de novo** (o e2e caiu num localizador
  que passou a achar dois botões; corrigido em db1110c1: 40 e2e + 398 Vitest verdes no worker) (398 Vitest, typecheck/lint/format
  limpos; e2e do team-list verde no worker). Botão "Marcar atendida" na linha do tablet parado; a frase "alguém
  tocou o tablet às HH:MM" na linha da sala; fixture da Guajajara alcança a frase. Sem bot na Mesa. **Mergear depois
  da API (792-A) e antes do #130.** https://github.com/shemaobt/facilitator-desk/pull/81
- [ ] **#130 · ENG-792 fatia C (app) — pronto, verificado por mim** (783 verdes, analyze limpo; CI verde; bot "nothing
  blocking", a corrida que ele apontou não existe porque person-arrived só carimba, quem solta é a releitura).
  **Mergear por último**, depois da A (API, seu merge) e da B (Mesa): este PR fecha a ENG-792.
  https://github.com/shemaobt/internalization-room/pull/130
- [ ] **#129 · ENG-741 (Keychain) — pronto, CI verde na re-rodada** (a primeira rodada caiu num teste que o PR não
  toca — oscilação medida: 14/15 no SHA do PR, 6/6 na main, 3/3 no merge local; suíte no merge local 784 verdes).
  **Mergear antes do #130.** Emenda 2 feita: uma escrita recusada pelo Keychain depois da coleta não re-coleta; o app guarda em
  memória e retenta só a escrita. Bot "nothing else from my side" no SHA final 23543b29.
  Segue a parte antiga: (o bot achou que uma escrita recusada pelo Keychain logo depois da coleta viraria re-coleta, 403 e vínculo apagado; o app passa a guardar em memória e retentar só a escrita). Quando fechar, peço a sua palavra para mergear. A credencial do tablet sai do
  `vinculo.json` e vai para o Keychain (`flutter_secure_storage` 11, `first_unlock_this_device`; sobrevive a
  reinstalação, que é o desejado); migração única de um arquivo antigo; esquecer esquece os dois. Dois achados no
  caminho, ambos corrigidos: uma leitura do Keychain que falha antes do primeiro desbloqueio não pode virar
  "nunca coletou" (o servidor responderia 403 e o vínculo inteiro seria apagado) — o cofre agora distingue
  "ausente" de "indisponível" e o app só olha de novo; e a migração tolera o cofre travado sem lançar. Verificado:
  757 verdes; caso 7 vermelho com o notifier anterior; tabela de mutação no PR (uma mutação sobreviveu e o caso 4
  foi reforçado). **Atenção:** `pubspec.lock` muda (dependência nova); `ios/Podfile.lock` não foi tocado — o seu
  próximo `flutter run` regenera os pods. CI e bot rodando no SHA final bdbceb5.
  https://github.com/shemaobt/internalization-room/pull/129

- [x] ~~ENG-741 · Keychain~~ — aprovado 07/09; em curso (worker Estojo, worktree `eng-741`).
- [x] ~~Revisão linguística en/es da Mesa (#79)~~ — textos aprovados por você em 07/09.
- [ ] **ENG-595 · App Store.** Só suas contas: registro, certificado, rótulos de privacidade, screenshots de iPad,
  ficha em português, notas ao revisor com o caminho por voz, TestFlight.
- [ ] **Mergear a corrente do app do outro fluxo** (#100 → #96 → #111 → #112 → #113 → #115 → #117 → #116 → #101, na
  Tasks for Henok). É o que destrava a 666/665 — as duas tocam o mesmo `session_notifier.dart`.

---

# Em execução — retomada em 07/09 (a corrente do outro fluxo entrou na main; ENG-666 → 665 destravadas)

1. ~~ENG-790~~ · no topo, PR #128 pronto.
2. **ENG-792** · as três fatias **em curso em paralelo**: A (API, Verruma), B (Mesa, Grosa), C (app, Lixa), B e C contra
   o contrato da A.
3. ~~ENG-666 → 665~~ · no topo, PR #127 pronto.

**Não peguei, de propósito:** ENG-688 (Oral Collector, não é da Sala) e ENG-711 (bot na Mesa; você decidiu não instalar).

---

# Feito — 39 PRs, 36 issues, três repositórios

**08/09, 00h — mergeados por mim no app, com a sua autorização:** #127 · ENG-666 + ENG-665 (a retrotradução
retomada começa no cursor; a 665 fecha por enumeração, sem frase falada) e #128 · ENG-790 (o círculo do
facilitador fica verde num aviso; a deixa de fala vence o verde).


**04/09:** #79 (Mesa, 609-2) · #124 (app, 609-3) · #337 (API, 610) · #336 (API, 609-1) · #122 (app, 625) ·
#333 (API, 624) · #332 (API, 456) · #120 (app, 623) · #331 (API, 645) · #330 (API, 622) · #119 (app, 645).
**03/09:** #329 (API, 729) · #118 (app, 667) · #313 (API, 605) · #78 (Mesa, 605) · #77 (Mesa, 713).
**02/09 e antes:** #308, #307, #306, #304, #302, #301 (API) · #109, #108, #107, #106, #105, #104, #103, #102, #99,
#98, #97, #95, #93, #92 (app) · #75 (Mesa).

Issues Done: 453, 456, 473, 474, 501, 559, 602, 605, 609, 610, 622, 623, 624, 625, 629, 630, 634, 635, 636, 637,
638, 640, 645, 646, 664, 667, 687, 699, 708, 709, 713, 722, 729. Abertas nesta rodada: 741, 790, 792.