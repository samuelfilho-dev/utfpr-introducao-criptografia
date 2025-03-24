import unicodedata

def normalize_text(text):
    return ''.join(
        c if c in ALPHABET else unicodedata.normalize('NFD', c).encode('ascii', 'ignore').decode('utf-8')
        for c in text
    )

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    msg = normalize_text(msg)
    key = normalize_text(key)
    encrypted_text = []
    key = generate_key(msg, key)
    
    for i in range(len(msg)):
        char = msg[i]
        if char in ALPHABET:
            new_index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % len(ALPHABET)
            encrypted_text.append(ALPHABET[new_index])
        else:
            encrypted_text.append('')  # Remove caracteres especiais
    
    return "".join(encrypted_text)

def decrypt_vigenere(msg, key):
    msg = normalize_text(msg)
    key = normalize_text(key)
    decrypted_text = []
    key = generate_key(msg, key)
    
    for i in range(len(msg)):
        char = msg[i]
        if char in ALPHABET:
            new_index = (ALPHABET.index(char) - ALPHABET.index(key[i])) % len(ALPHABET)
            decrypted_text.append(ALPHABET[new_index])
        else:
            decrypted_text.append('')  # Remove caracteres especiais
    
    return "".join(decrypted_text)

# with open('./aula_02/poema.txt', 'r') as file:
#     poema_text = file.read()

# key = 'emily'

# poema = encrypt_vigenere(poema_text, key)
# print(f"{poema}")

# print("-------------------")

# with open('./aula_02/misterio.txt', 'r') as file:
#     misterio_text = file.read()

# misterio_key = 'rodrigo'

# decrypted_text = decrypt_vigenere(misterio_text, misterio_key)
# print(f"{decrypted_text}")

print("-------------------")
with open('./aula_02/text_01.txt', 'r') as file:
    text_01 = file.read()

print(f"{encrypt_vigenere(text_01, 'andrade')}")


print("-------------------")
with open('./aula_02/text_02.txt', 'r') as file:
    text_02 = file.read()

print(f"{encrypt_vigenere(text_02, 'claricelispector')}")



print("-------------------")
with open('./aula_02/text_03.txt', 'r') as file:
    text_03 = file.read()

print(f"{encrypt_vigenere(text_03, 'hunterhunterhunter')}")