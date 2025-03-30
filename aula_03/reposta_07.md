## Pesquise o porque do protocolo WEP adicionar um IV (initialization vector) junto com a senha secreta da rede antes de utilizar o algoritmo RC4. Liste as redes de internet Wi-Fi para determinar que tipo de algoritmo criptografico utilizam.

    O adicionamento do IV (Initialization Vector), acontece devido a fato de usar o mesmo texto para a criptografia pode exibir o mesmo resultado, logo um atacante pode obter pistas mas descriptografar a mensagem. Além de impedir ataques por força bruta usando rainbows tables por exemplos. 

    O IV é um valor aleatório adicionado a mensagem crua como uma tentativa que isso não ocorra.

- WEP
    - **Protocolo**: RC4
    - **Método de autenticação**: CRC
    - **Tamanho da chave**: 10 a 32 dígitos HEX
    - **Nível de segurança**: Fraco
- WPA
    - **Protocolo**: TKIP
    - **Método de autenticação**: PSK
    - **Tamanho da chave**: 8 a 64 caracteres
    - **Nível de segurança**: Médio
- WPA2
    - **Protocolo**: AES
    - **Método de autenticação**: PSK
    - **Tamanho da chave**: 8 a 64 caracteres
    - **Nível de segurança**: Alto
- WPA3
    - **Protocolo**: AES
    - **Método de autenticação**: SAE
    - **Tamanho da chave**: 8 a 64 caracteres
    - **Nível de segurança**: Altíssimo


## Fontes
 - [TecnoBlog](https://tecnoblog.net/responde/o-que-e-wep-wpa-wpa2-wpa3-diferencas-protocolo-seguranca-wi-fi/)
 - [techtarget](https://www.techtarget.com/whatis/definition/initialization-vector-IV)
