#### TODO Agent

**Estação Rever — CONCLUÍDA e na main**

- [x] **ENG-730** (PR #217, `5d91ec7`) — ajuste do dono depois de andar na tela: o colar rola dentro da própria janela (mesmo `maxHeight` de Escuta/Frases), a legenda das marcas saiu (e com ela o slot `aside` do `StationNav`, que só existia para ela), e o conteúdo passou a ser centrado verticalmente com viewport fixo e rodapé preso. O segundo commit foi 1 linha de CSS e 169 de teste de navegador provando os dois casos — história curta e longa, com guarda contra teste vazio.

O fluxo agora é **Ouvir → Cortar → Triagem → Frases → Rever**, e concluir a história virou ato consciente em vez de efeito colateral da última frase.

- [x] **ENG-725** (PR #214, `4a62da0`) — o panorama: colar inteiro com fim de frase distinto de fim de cena, fila de pérolas com a confiança no próprio preenchimento, barra de cinco estações, aviso de segundo toque, tela de conclusão com uma pérola por cena.
- [x] **ENG-702** (PR #215, `e250d4b`) — concluir de verdade. `complete()` perdeu o parâmetro de artefatos e o upload multipart; a sessão finalmente vira Concluída no painel. Numa falha de rede a tela de parabéns não sobe e o mesmo botão tenta de novo.
- [x] **ENG-726** (PR #216, `19691dd`) — a gaveta de cobertura na Rever: resumo da história, cena a cena, contagem por tipo, candidatos a ausência. Só facilitadora, nasce fechada, e fechada não vaza dígito nenhum.

Verifiquei as três por mim, não pelo relato: suíte, typecheck, lint e depcruise rodados aqui; diffs lidos; capturas conferidas contra o desenho; e na ENG-702 rodei os testes novos **contra a main** numa worktree descartável — os quatro falham lá. Nenhum arquivo de código em `domain/` ou `contracts/` foi tocado nas três.

**Dois bugs pré-existentes que a Rever expôs e consertou** (nenhum seria pego por teste — só por olho na tela): o contraste dos tracinhos da barra no tema claro, invisíveis sobre o preenchimento; e o transbordo da contagem por tipo na gaveta, que cortava o alvo de cada tipo — consertado na fonte, então a Triagem melhorou junto.

**Abertas, nenhuma é da Rever**
- [ ] **ENG-727** — a emulação de `prefers-reduced-motion` do Playwright não está em vigor no headless shell. Toda a suíte e2e roda com animação ligada acreditando que está desligada: fábrica de flake por tempo, e nenhum teste exercita o caminho de movimento reduzido, que é requisito de acessibilidade.
- [ ] **ENG-728** — o caminho de LEITURA de artefatos está morto por construção: `getArtifacts()` sempre lança depois de um complete. Toca `contracts/`, exige revisão humana.
- [ ] Áudios do piloto — parado a pedido do dono.

**Corte de escopo — concluído e no ar** (ENG-689, ENG-691, #298 no `shema-api`, ENG-677, ENG-700). Produção: https://soundnecklace.shemaywam.com

Nenhum worker ativo. Nenhum PR aberto. Nada em execução.