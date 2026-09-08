# TODO Maestri

**05/09. Fila vazia. Nenhuma PR aberta. A ENG-701 entrou e está no ar.**

---

## Estado

    main       845dae9   #74 mergeada — a escala com degrau miúdo
    escala     12 · 13 · 15 · 16 · 18 · 20 · 21  (display 29, banner 38)
    PRs        nenhuma aberta
    workers    Régua (sonnet) — ENG-614, worktree .worktrees/s614
    local      dois dev servers derrubados

**Conferido no artefato servido em producao**, nao no relatorio do deploy: o bundle `/assets/index-Wz9K4zKu.css` em `facilitatordesk.shemaywam.com` entrega 12 · 13 · 15 · 16 · 18 · 20 · 21, com display 29 e banner 38.

**Verificado por mim antes do merge, não pelo relato:** ramo rebaseado em `b13a294` e 0 commits atrás; diff sem nenhum componente tocado; os nove nomes de token idênticos ao `TYPE_SCALE` do `cn.ts`; os nove `line-height` sem unidade. Três jobs verdes no CI (`verify` 2m48s, `docker-build` 1m26s, `e2e` 14m55s), mais 200/200 no macOS e 200/200 no contêiner pelo worker.

## Próximas fatias, especificadas e não começadas

**ENG-825** (Todo, alta, 2) — **aberta hoje, e é a mais grave da rodada.** O `src/i18n/locales.test.ts` acha as chaves com `/\bt\(\s*"([^"]+)"/g`, literal **imediatamente** depois de `t(`. Toda chave escolhida por ternário é invisível. Medido por mim sobre `src/` em `a5915cb`: **202 chaves vistas, 18 invisíveis**, todas na Mesa. A ENG-614 provou o custo plantando um typo — lint, typecheck e Vitest verdes, e o que renderizou foi **a chave crua como nome acessível**. Duas das dezoito estão nesse buraco há meses; a ENG-614 não criou a categoria.
**Não alargar o regex para "qualquer literal dentro de `t(`"** — varreria os mapas de classe Tailwind e os fragmentos do `REFUSAL_KEY` que o próprio arquivo exclui de propósito, e a razão escrita lá continua valendo.

**ENG-614** (Todo, alta) — a reserva de altura. Critério de aceitação escrito e já vermelho em `~/.maestri/handoff/eng-614/`. Precisa também **comitar o `no-truncation.spec.ts`**, porque `CLAUDE.md:2871` e `:4562` já o referenciam e o arquivo não existe na main. **Sem número herdado:** medir a base com `npm run census`, que agora tem a escala nova e as peças da #78 e #79 na tela.
**ENG-654** — o `link-device.spec.ts` afirma que a recusa existe, nunca que ela está na tela.

## Do dono, tudo na nota dele

Credencial real · reemitir o `CLAUDE_CODE_OAUTH_TOKEN` · mergear `shemaobt/.github#7` · entrar e apertar play · o cross-fade de 400ms · ENG-474.

---

## O que ficou aprendido

**Suspeitar do próprio instrumento antes de suspeitar da auditoria alheia.** Medi 14,22px contra os 10,83px da auditoria e anunciei a auditoria como imprecisa. O errado era o meu filtro: `sr-only` recorta a 1px, tem caixa, e 5669 dos 7919 caracteres eram texto de leitor de tela.

**Um censo envelhece quando a tela ganha peças.** Eu disse 61,8%; com a coluna de sessões (#78) e as salas paradas (#79) na tela são 62,1%. Medir de novo depois que a main anda, não reusar o número.

**Verde de CI contra base morta não é verde.** A #74 passou nos três jobs contra uma base de 11 commits atrás, e o que ela nunca tinha renderizado eram justamente os componentes novos da Mesa.

**O cheiro que denuncia:** se um balde de tamanho não se mexe quando todos os tokens mudam, aquele texto não passa por token nenhum. Foi assim que se provou que `SessionCard`, `SessionsColumn` e `HaltedRoomsSection` respeitam a escala.

**Um piso medido onde eu olhei não é o piso.** Dei 17px; o pior par real da base era 3,41px, noutro idioma noutra tela — e não era encostar, era sobrepor, até −15,84px.

**Um portão vale o que ele avermelha.** O piso que desceu de 14 para 12 só vale porque foi provado vermelho contra `31d5a47`, seis vermelhos nomeando 9 a 11,5px.