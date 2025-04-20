## Este exercício é aberto para que voce possa descrever alguma etapa do algoritmo AES em detalhes.

A etapa de MixColumns é uma etapa no qual se faz uma transformação linear ás colunas da matriz, contribuindo para o principio da difusão, espalha a informação no bloco.

Cada colunas da matriz é multiplicada por uma matriz 4x4 no campo finito de GF(2^8), ou Galois Field (Campo de Galois), o 2^8 representa um campo de Galois de 256 elementos de um campo de 8 bits. E as operações adição e subtração são feitas com XOR bit a bit. Além de a multiplicação é feita como multiplicação de polinômios, mas módulo um polinômio irreduzível de grau 8. Sendo o polinômio irreduzível no AES:

```txt
m(x) = x⁸ + x⁴ + x³ + x + 1 = 0x11B (em hexadecimal)
```

Logo terá uma coluna como resultado:
```txt
[ (02•a0) ⊕ (03•a1) ⊕ (01•a2) ⊕ (01•a3) ]
[ (01•a0) ⊕ (02•a1) ⊕ (03•a2) ⊕ (01•a3) ]
[ (01•a0) ⊕ (01•a1) ⊕ (02•a2) ⊕ (03•a3) ]
[ (03•a0) ⊕ (01•a1) ⊕ (01•a2) ⊕ (02•a3) ]
```
Garantindo uma permutação complexa para não ajudar uma possível criptanalise da mensagem, garantindo seu trafico seguro.  