#### TODO Agent

**Backlog — não pegar sem o Henok pedir**
- [ ] ENG-535 · nenhum código que só roda no navegador é exercitado por teste (`kIsWeb` cru: 97 no projeto, 66 como decisão de ramo em gravação)
- [ ] ENG-523 · limpeza de segmentos órfãos com `dart:io` cru, sem relato, nos dois notificadores

**Recorrente**
- [ ] Recriar a `dev` a partir da `main` depois de cada release
- [ ] ENG-408 no aparelho: pedir a frase exata do erro na próxima ocorrência

**Restrições ao planejar**
- Duas fatias que editam `.arb` não podem correr em paralelo
- As fatias que tocam os notificadores de gravação vão em sequência
- "mergeable clean" do GitHub não garante merge são: simule o merge e rode a suíte antes
- `build web` **não** prova fronteira de plataforma — passa com `dart:io` no grafo do main
- Ramo decidido por `kIsWeb` cru é intestável na VM; use `isWebPlatformProvider` quando o ramo precisar de teste
- Teste de ramo de plataforma precisa de impressão digital (ex.: formato `webm` vs `m4a`)
- Screenshot de portal não captura canvas do Flutter — a tela sai branca mesmo com o app renderizando. Use os logs de acesso do nginx como evidência
- Worktree sempre de `origin/dev`; o checkout local da `main` está desatualizado