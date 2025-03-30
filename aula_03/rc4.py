import sys

def map_char (num):
   return chr(num)

def ksa(chave):
    permutacao = list(range(256))

    chave_numerica = [ord(c.upper()) - ord('A') + 1 for c in chave]

    j = 0
    for i in range(256):
        j = (j + permutacao[i] + chave_numerica[i % len(chave_numerica)]) % 256
        permutacao[i], permutacao[j] = permutacao[j], permutacao[i]

    return permutacao


def prga(tabela_de_permutacao):
    i = 0
    j = 0

    while True:
        j = (j + 1) % 256

        i = (i + tabela_de_permutacao[j]) % 256

        tabela_de_permutacao[i], tabela_de_permutacao[j] = tabela_de_permutacao[j], tabela_de_permutacao[i]

        yield tabela_de_permutacao[i]

file_out = open(sys.argv[3], 'w' , encoding='utf-8', errors='ignore')
chave = sys.argv[2]

permutation_table = ksa(chave)
keystream = prga(permutation_table)


with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as file_in: 
   for line in file_in:
      for char in line:
        cypher_byte = map_char(ord(char) ^ next(keystream))
        file_out.write(cypher_byte)
      file_out.write("\n")
file_out.close()
