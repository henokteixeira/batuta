#### TODO Henok

**Nada travado em você no momento.**

O corte de escopo está inteiro no ar, e o `.cds-scroll` do pacote de design foi corrigido na fonte (#212, mergeado).

Produção: https://soundnecklace.shemaywam.com — a URL direta do Cloud Run devolve 503 por origem não permitida no CORS; use sempre o domínio.

**A estação Rever está pronta e na main** — as três fatias mergeadas e verificadas por mim (ENG-725 `4a62da0`, ENG-702 `e250d4b`, ENG-726 `19691dd`). O bug que você relatou está resolvido: a sessão vira Concluída no painel.

**Para você decidir ou revisar**

- [ ] **Decidir o rótulo central do rodapé na Rever** — o desenho novo pede "Rever · a história inteira" em versalete no meio do rodapé. Mas o `nav-footer` guarda por escrito uma decisão sua: "versão enxuta que o dono pediu: só voltar e avançar, SEM o rótulo de contexto do centro". O desenho e essa decisão se contradizem, e quem desempata é você — eu não passo por cima. Mandei deixar o centro vazio por ora; se você liberar, entra em duas linhas. (A legenda das marcas — Certeza, Quase, Na dúvida, fim de frase, fim de cena — eu autorizei, porque sem ela o ouvinte não sabe ler o colar: é conteúdo, não enfeite de chrome.)

- [ ] **A celebração da meta não sobe mais sobre a Rever** — decisão minha, reversível, avise se discordar. Como chegar à Rever enche a barra, as metas "fechar as Frases" e "a história toda" passam a se cumprir no instante em que a estação monta, e a tela "A meta de hoje está no cordão" subiria por cima do panorama antes de vocês o verem. Isso destrói o motivo de a Rever existir. Então a meta continua se cumprindo em silêncio e o fecho celebratório fica só na tela oliva, que já diz "A história está completa". A alternativa seria as metas só se cumprirem no Concluir, mas isso mexe no modelo da barra para consertar um efeito colateral.

- [ ] **Revisar o plano da estação Rever** — sigo com estas premissas, todas tiradas do seu guia: a Rever é tela (não gaveta), os dois a veem (logo, nenhum número e tempo por extenso), **nada se edita ali** (a correção acontece na estação de origem), "nenhum se encaixa" é resposta e não erro, e a tela oliva de fim de bloco passa a vir **depois** de concluir, não depois das Frases. Reversível: se você discordar, eu refaço.

**Parado a seu pedido**

- [ ] **Áudios do piloto** — falta o tokenizador do `tripod-lab` nesta máquina; sem ele não há acousteme, e áudio sem acousteme não abre sessão. E a pasta nova é acervo terena geral, não a continuação do de Rute: o script tem `COLLECTION = "terena-ruth"` e o prefixo `ruth/` chumbados.
- [ ] Liberar (ou negar) meu acesso de leitura ao segredo `tripod_backend_neon_database_url`.

**Só para saber**

- Sua árvore de trabalho principal está parada em agosto (`5165d75`), com três arquivos de `docs/design/` apagados sem commit. Isso já me fez ler código velho uma vez. `git checkout -- docs/design/ && git pull` resolve.
- O protótipo v4 no repo é a forma-fonte do dc e **não abre no navegador** — falta o `support.js` ou um bundle exportado. Você lê o design como código hoje.
- Depois do corte, o produto **não tem uso de modelo nenhum**. As três exceções autorizadas eram todas da entrevista; a seção do `CLAUDE.md` foi mantida dizendo que a regra foi esvaziada por um corte de escopo, e que elas voltam por escrito se a entrevista voltar.