# como funciona

Em uma frase: você define com o Definidor, o Orquestrador executa, e você só responde o que está em "pra você".

## Antes de cada rodada

1. Abra o Definidor e traga a lista: tickets sem definição, defeitos vistos num teste, ideias, e as linhas "Definir:" que o Orquestrador deixou em "pra você". Serve tanto para o que já está no Linear quanto para o que ainda não é ticket.
2. Ele grelha item a item, uma fronteira por vez, cada pergunta com a resposta recomendada. Responda ditando. Fatos ele busca; a você só vão decisões.
3. Ele atualiza o glossário, escreve ADR quando a decisão é difícil de reverter, publica spec e tickets no Linear com bloqueios, e só rotula `ready-for-agent` o que tem regra em uma frase, critério de aceitação testável e zero decisão pendente.

## Durante a rodada

4. Diga ao Orquestrador para começar. Ele puxa os tickets `ready-for-agent` sem bloqueio, escreve o plano de fatia, cria o worktree, recruta um executor com o modelo do ticket e despacha. Três tarefas no máximo, uma grelhando você por vez.
5. Você olha só "pra você". Cada linha é uma pergunta fechada ou uma aprovação de alto risco. Responda ali e a linha some. O painel mostra o andamento.
6. O Orquestrador verifica cada PR contra os testes e contra a spec, espera a CI, registra as decisões no ticket e reinicia o executor. Mudança visível você olha no portal ou no simulador.

## No fim

7. Ele escreve a nota de estado no fichário logs e termina com TASK_COMPLETE ou BLOCKED. Achados viram ticket ou são descartados.
8. A próxima rodada começa com o Orquestrador reiniciado, lendo a nota de estado. As notas são a memória; a sessão não é.

## Paralelismo alto

Peça ao Definidor uma rodada de alta autonomia. Ele fecha a fila inteira primeiro e escreve `modo: alta autonomia` no painel. O Orquestrador dispara toda a fronteira de uma vez e apaga a linha ao encerrar. Nunca é o padrão.

Texto completo: ~/Documents/programming/batuta/docs/fluxo.md
