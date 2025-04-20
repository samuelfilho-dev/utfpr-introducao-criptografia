## Qual o principal módulo, em termos de segurança, no algoritmo DES?

<p align="justify">
O Principal módulo de um DES é etapa de substituição, as S-boxes.

Durante a etapa de substituição, o texto simples sofre uma transformação não linear usando oito S-boxes diferentes. Cada S-box é uma tabela 4×16, onde cada linha representa uma entrada de 4 bits e cada coluna representa uma saída de 4 bits. As S-boxes são derivadas de uma permutação fixa dos números de 0 a 15. A entrada para cada S-box é um valor de 6 bits obtido na etapa de permutação anterior.

São responsáveis pela implementação a operação de confusão no processo de criptografia. Ela garante que um bit do plan text dependa de vários bits do cypher text e a key do algoritmo  
<p>

