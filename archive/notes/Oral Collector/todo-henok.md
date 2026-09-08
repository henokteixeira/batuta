#### TODO Henok

- [ ] **Mergear a PR de release #245** (dev → main, 1.6.0+240) — https://github.com/shemaobt/oral-collector/pull/245
- [ ] Antes de mergear, o que sobrou do gate de CSP (ENG-169) e só você pode fazer, porque exige conta e backend real: login, gravação + upload, playback do GCS, e conferir os glifos não-latinos na tela. O resto do gate eu verifiquei e está registrado na issue
- [ ] Depois do merge: o `delete_branch_on_merge` apaga a `dev`, e eu a recrio a partir da `main`
- [ ] Tirar o `push: branches: [main]` do `google-play.yml` e do `testflight.yml`, deixando só o `workflow_dispatch`. É o que dá a condição de "deploy só web". Muda seu processo de release
- [ ] Áudio da era 14/05–12/08: arquivos no disco dos aparelhos, sem linha nem metadado. Recuperar = varrer o diretório e oferecer áudio anônimo para a pessoa classificar do zero. Três saídas: (a) abro a issue de recuperação, (b) abro só uma issue que **conta** quantos são, para decidir com número, (c) deixamos quieto