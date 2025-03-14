from collections import Counter

def contar_caracteres(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.replace(" ", "").replace("\n", "").replace("\t", "")
            return Counter(text)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None


chars = contar_caracteres("./aula_01/misterio.txt")

if chars is not None:
    for char, freq in chars.items():
        print(f"'{char}': {freq} \n")
