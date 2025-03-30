## Pesquise e descreva o uso do algoritmo RC4 em Ransomwares.
O algoritmo mais usando em Rasonwares é o RC4 pela fácil implementação customizada do código. O algoritmo RC4 é do tipo criptografia simétrica, logo ele usa a mesma chave para criptografar e descriptografar os dados. Podendo ser uma chave de 1–256 bytes de caracteres aleatórios

 - **1º Passo:** 
    - O algoritmo cria um array no qual cada valor é igual a sua posição no array, podendo ir de 0 a 256. O array é gerado de forma pseudoaleatória a partir de uma chave e seu output será uma tabela de permutação. O algoritmo irá realizar esta ação em formato de um loop for, 256 vezes.
    - Implementação Python
    ```python
    def ksa(chave):
        # Inicializa a tabela de permutação.
        permutacao = list(range(256))

        # Percorre a chave fornecida.
        for i in range(len(chave)):
            # Gera um índice aleatório.
            indice_aleatorio = i % len(permutacao)

            # Troca os elementos da tabela de permutação.
            permutacao[i], permutacao[indice_aleatorio] = permutacao[indice_aleatorio], permutacao[i]

        return permutacao
    ```
 - **2º Passo:** 
    - A tabela de permutação criada pelo KSA, passará por outro algoritmo de criação de sequência pseudoaleatória chamando de Pseudo-Random Generation Algorithm (PRGA), nele será gerado a `keystream` responsável por encriptar os dados que estão em seu formato original (plaintext).
    ```python
    def prga(tabela_de_permutacao):
    # Inicializa os índices i e j.
    i = 0
    j = 0

    # Gera um número aleatório.
    while True:
        # Gera um novo índice j.
        j = (j + 1) % 256

        # Gera um novo índice i.
        i = (i + tabela_de_permutacao[j]) % 256

        # Troca os elementos da tabela de permutação.
        tabela_de_permutacao[i], tabela_de_permutacao[j] = tabela_de_permutacao[j], tabela_de_permutacao[i]

        # Retorna o elemento na posição i da tabela de permutação.
        return tabela_de_permutacao[i]
    ```
 - **3º Passo:** 
    - Nesse passo acontece a operação XOR, onde de fato ocorre o processo de encriptação dos dados utilizando as funções dos passos anteriores. Para que ocorra a função recebe a chave secreta e os dados que serão encriptados (ou decriptados). 
    - E no corpo da função principal, irá ser executado os passos do KSA e PRGA, para que enfim, seja feita uma operação XOR entre a KeyStream e os dados em formato original. O resultado da operação XOR, será a encriptação.
    ```python
    def xor(dados, chave):
    # Gera a tabela de permutação pseudoaleatória.
    tabela_de_permutacao = ksa(chave)

    # Gera a KeyStream.
    stream = prga(tabela_de_permutacao)

    # Combina os dados em formato original com a KeyStream,
    # por meio de uma operação XOR.
    for i in range(len(dados)):
        dados[i] = dados[i] ^ stream()

    return dados
    ```

O algoritmo RC4 é usando no Rasonware REvil, como desmotra o artigo no qual o através do uso de engenharia reversa, nela pode observar a função `FUN_0040110b` no que ela recebe um parâmetro, uma variável local local_124 que tem o tamanho de 256 bytes. Podendo indicar o uso do RC4. Além de o endereço de memória da variável local `local_124` foi atribuía ao `param_1`, recebido na função anterior. Indicando um binário que inicia um processo de loop iterando 1 a cada rodada. Logo pode conclui o uso de RC4 em Rasonware como processo de criptografar seus dados.


## Fontes 
 - [[Engenharia Reversa] Reconhecendo a Implementação Customizada do Algoritmo RC4 no REvil Ransomware](https://0x0d4y.medium.com/engenharia-reversa-reconhecendo-o-implementa%C3%A7%C3%A3o-customizada-do-algoritmo-rc4-no-revil-ransomware-44e2aff2fd6a)