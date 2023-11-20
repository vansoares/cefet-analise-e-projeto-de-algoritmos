
#### NP-Completude
Constante, linear e quadrático são exemplos de tempo polinomial (vêm na forma de O(n^x)).
Existe uma grande diferença de tempos entre polinomial, exponencial e fatorial. O conceito de NP-Completude ajuda a classsificar problemas de acordo com sua complexidade computacional. 
Existem 4 categorias de problemas:
##### P
Soluções são em tempo polinomial.

##### NP
Problemas polinomiais não determinísticos. 
Problemas onde uma solução proposta pode ser verificada em tempo polinomial. Porém, encontrar a solução de fato requer um tempo exponencial ou fatorial.

**-> NP-Completo**
- Possui uma propriedade: se for encotnrada uma solução para um problema NP completo em tempo polinomial, pode-se resolver todos os problemas NP em tempo polinomial.

**-> NP-Difícil**
- São relacionados aos NP-Completo, porém diferentes. 
- Não possuem processor de verificação eficientes como os de NP, mas servem de referência para problemas que são extremamente difíceis de resolver em nível computacional. 
#### Bin Packing
Dados n itens de tamanho s1, s2, s3, ..., empacotá-los no menor número de caixas possível
- Não existe nenhum algoritmo de tempo polinomial para essa solução, por isso é dado como se não existisse; 
- Exemplos de aplicações:
	- Encher lixeiras de reciclagem
	- Encher cargas de caminhões
	- Gravar fitas de músicas
- Heurísticas: (olhar https://www.youtube.com/watch?v=qbuMPi44bVQ)
	- Next-Fit
	- First-Fit
	- Best-Fit
	- First-Fit Decreasing
	- Best Fit Decreasing




### Links Úteis
- https://developers.google.com/optimization/pack/bin_packing?hl=pt-br
- https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
- https://en.wikipedia.org/wiki/Bin_packing_problem
- https://www.youtube.com/watch?v=qbuMPi44bVQ
- https://freedium.cfd/https://towardsdatascience.com/np-what-complexity-types-of-optimization-problems-explained-558d43276044