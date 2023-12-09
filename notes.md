### Notes

- TODO
    - Implementar abordagem com peso e valor
    - Testar diferentes pesos e tamanhos de mochila
    - resolver problema da notação cientifica do tempo do guloso
    - contar quantos itens foram deixados de fora por terem peso maior que a capacidade do bin

### Força bruta 
- Máximo de 11 itens que retornam algum resultado
- Com 12 itens na segunda iteração já da erro
- Com poucos itens, chega a ser mais rapido que o guloso. Mas conforme o numero de itens aumenta, vai ficando mais lento

### Guloso
- Roda com 600k itens (máximo que testei por enquanto)


##### com pesos e valores
iteracoes = 30
capacidade da mochila = 10
Quantidade de itens | Tempo Força bruta | Tempo Guloso
5 | 0.0008625 | 0.000012 
7 | 0.024973 | 0.000011
9 | 2.746610 | 0.000022
10 | 42.027788 | 0.000023
11 | - | 0.000023
100 | - | 0.0008861 
1000 | - | 0.06701743

iteracoes = 30
capacidade da mochila = 100
Quantidade de itens | Tempo Guloso
1000 | 0.06701743
10000 | 3.8666609
100000 | 274.54763


##### pesos
iteracoes = 30
capacidade = 10
Quantidade de itens | Tempo Força bruta | Tempo Guloso
5 | 0.000551 | 0.000009
7 | 0.013468 | 0.000005
9 | 1.212578  | 0.000006
10 | 13.773826  | 13.773826
11 | Estouro de memoria  | 0.000014
100 |  - | 0.000102
1000 |   | 0.000550



iteracoes = 30
capacidade = 100
Quantidade de itens |  Tempo Guloso
10000 |   0.010057
100000 | 0.570911
500000 |20.146856