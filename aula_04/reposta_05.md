## Utilize o código `ides.c` (Simplified-DES para imagens) para criptografar a imagem `lena.pgm` e `arma.pgm` com a técnica ECB (que ja esta implementada). Questão: é possível do conte ́udo da imagem? Modifique esse código para utilizar alguma outra técnica por bloco (por exemplo CBC). Agora  ́e possível ter noção do conte ́udo da imagem? Atribua zero para o vetor de inicialização (IV)

#### Reposta 01
Não é possível, pois o arquivo fica em linguagem de máquina, o IrfanView não foi capaz de abir a imagem.


O arquivo a `lena.pgm` cifrada se encotra na `lena-cypher.pgm`.

#### Resposta 02
Criei o arquivo `sdes-cbc.c` para criar um DES usando CBC, mesmo assim não foi possível abrir o arquivo o pois 
o algorítimo deixa o arquivo em linguagem de maquina. 

O arquivo a `arma.pgm` cifrada se encotra na `arma-cypher.pgm`.