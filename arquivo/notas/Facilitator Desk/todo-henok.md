# TODO Henok

**05/09. Nada meu pendente. Seis linhas tuas, nenhuma bloqueando outra.**

---

## [x] A palavra TRANSCRIÇÃO some do cartão — decidido em 07/09

**"pode deixar sem a palavra, só ícone mesmo".** A divulgação fica como quarto controle de 44×44 na linha de tocar / Responder / Falar pessoalmente, só com o galo; a palavra vive no nome acessível (`showTranscript`/`hideTranscript`). Leitor de tela continua ouvindo a frase inteira.

<details><summary>o porquê, para o registro</summary>

## [x] A palavra TRANSCRIÇÃO some do cartão — decisão tua

A ENG-614 (PR #80) tira a divulgação da linha própria e a põe como **quarto controle de 44×44 na linha que já tem tocar, Responder e Falar pessoalmente**. Com quatro alvos dividindo os 391px da linha **não sobra largura para a palavra**, então ela virou só o galo (chevron) num círculo, e a palavra passou a viver apenas no nome acessível — duas chaves novas, `showTranscript`/`hideTranscript`.

**O que se ganha:** a altura de volta em todo cartão, aberto ou fechado, e é ela que paga a quebra de linha do título — o `truncate` saiu, a pergunta não é mais cortada.

**O que se perde:** o facilitador que varria a coluna procurando a palavra agora precisa aprender um ícone. Leitor de tela continua ouvindo a frase inteira; olho nu, não.

É coerente com os outros dois controles da linha, que já são só ícone.

</details>

## [x] O plano da ENG-614 — as premissas que valeram

Segui sem esperar, porque era reversível, e nenhuma premissa caiu:

Despachei sem esperar, porque e reversivel. As premissas, para tu discordares se quiser:

- **A forma:** a divulgacao da transcricao sai da linha propria e vai para a linha que ja tem tocar, *Responder* e *Falar pessoalmente*; o `truncate` sai do titulo. As duas juntas, numa fatia so — foi a tua decisao de 29/08, opcao (a) com sequencia.
- **O que eu proibi:** encolher controle, encolher tipo, ou afrouxar o piso de dois cartoes para caber. Se os quatro controles nao couberem numa linha a 1024 em espanhol — que a propria issue diz que **ninguem mediu** — ele para e me traz a medida, e eu te trago a decisao.
- **O que eu mandei ignorar:** todo numero da issue e do README. Foram escritos em 28-29/08, antes da ENG-697 e da ENG-701. Os 44px, os ~40px por cartao, os 14px de deficit em pt/es — todos de uma tela maior.

**Uma coisa que a issue admite e vale tu saberes:** "a transcricao fica quase sempre fechada" e **leitura de design, nao observacao** — nao existe telemetria. A fatia inteira gasta o orcamento nessa premissa.

## [ ] Uma credencial real, para a Mesa sair do dublê

A ligação com a API local **está provada**: a aplicação manda `POST /api/auth/login` e o `tripod_backend` responde. Falta conta.

Medido no código (`httpFacilitatorService.ts:95`): depois do login a Mesa pergunta `/auth/me` e `/auth/my-roles?app_key=<sala>`, e só abre para **admin de plataforma** ou **portador do papel de facilitador**. Cadastro simples loga e apanha na porta seguinte.

- **Uma conta que já exista e já tenha o papel**, por variável de ambiente na linha de comando — nunca dentro de arquivo; ou
- **autorização para eu criar uma** por `/api/auth/signup`, sabendo que isso **escreve no `tripod_db`**, que é o teu banco de verdade, e que conceder o papel é outro passo.

**Destrava:** eu conferir a Mesa contra dado real. Hoje toda verificação minha e todo o CI rodam sobre dublê.

## [ ] Reemitir o `CLAUDE_CODE_OAUTH_TOKEN` deste repositório

Medido: a review morre no turno 1, em 176ms, `total_cost_usd: 0`, `modelUsage: {}`. O mesmo workflow revisou o `shema-api` com sucesso duas vezes; lá o segredo é de 30/07, aqui de 25/08. `HENOKINHO_APP_ID` e `HENOKINHO_APP_PRIVATE_KEY` estão bons.

**Destrava:** a review automática em toda PR daqui. **Treze PRs entraram sem revisão de gente nesta semana.**

## [ ] Mergear `shemaobt/.github#7`

Aberta, revisão pedida ao João. **A ordem:** primeiro a #7, depois o token, depois rotular uma PR com `henokinho`. Enquanto o `uses:` apontar para um `@main` sem o ramo do rótulo, o check sai `skipping`.

## [ ] Entrar e apertar play

O caminho do áudio **nunca foi exercitado ponta a ponta em produção**. Nenhum teste alcança isso.

## [ ] O cross-fade de tema a 400ms

Fura o teto de 300ms da §4. Ou o cross-fade desce, ou a §4 sobe.

## [ ] ENG-474 — reescrever em vez de fechar

`8db0b59` fecha o que a issue pede, mas **três linhas do escopo seguem abertas**. Fechar apaga as três.

---

## No ar

    main 845dae9 — a ENG-701 entrou
    escala servida  12 · 13 · 15 · 16 · 18 · 20 · 21  (display 29, banner 38)
    domínio  https://facilitatordesk.shemaywam.com   HTTPS 200, mapeamento Ready

**O número, para ficar registrado:** 62,1% da Mesa é desenhado abaixo de 14px agora — 51,3% a 12px mais 10,8% a 13px. É a inversão do `61,8% -> 0,0%` que a ENG-652 publicou como conserto. Não é regressão: é o teu pedido cumprido duas vezes. Se a queixa voltar, o que eu mediria é o **line-height e o topo da escala**, não o piso outra vez — a Mesa ganhou degrau miúdo e continua sem degrau grande, o maior tipo da tela densa são 18px em treze caracteres.

Censo contra a main anterior, com as peças da #78 e #79 na tela:

    mesa   2264 car.   média 14.88 -> 13.26   menor 14 -> 12
    lista  1240 car.   média 15.95 -> 14.23   menor 14 -> 12
    login   425 car.   média 18.85 -> 17.45   menor 15 -> 13

Treze PRs mergeadas nesta semana: #66 #67 #68 #69 #70 #71 #72 #73 #74 #75 #77 #78 #79. **Nenhuma revisada por gente** — o João foi pedido em todas, o bot nunca rodou.

## O teu ambiente local

    front   PARADO — as portas 5173 e 5174 estao livres
    API     tripod_backend :8000      Up, healthy, 245 rotas sob /api
    banco   tripod_db :5432           Up — o de verdade, eu nao encosto

Para subir: `cd /Users/henok/Documents/programming/obt/facilitator-desk && npm run dev`. **Puxa a main antes**, senão sobe sem a escala nova.

`.env.local` criado e ignorado pelo git; `VITE_API_BASE_URL=/api` é o interruptor. **Apaga esse arquivo antes de rodar `test:e2e`** — a suíte reusa a 5173 e passaria a medir a API real em vez do dublê que o CI mede.

## Próximas fatias, já especificadas

**ENG-614** (Todo, alta) — a reserva de altura; critério de aceitação já escrito e já vermelho em `~/.maestri/handoff/eng-614/`.
**ENG-654** — `link-device.spec.ts` afirma que a recusa existe, nunca que ela está na tela.