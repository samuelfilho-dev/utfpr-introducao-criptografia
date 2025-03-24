def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)
with open('./aula_02/poema.txt', 'r') as file:
    poema_text = file.read()

key = 'emily'

poema = encrypt_vigenere(poema_text, key)
print(f"{poema}")

print("-------------------")

with open('./aula_02/misterio.txt', 'r') as file:
    misterio_text = file.read()

misterio_key = 'rodrigo'

decrypted_text = decrypt_vigenere(misterio_text, misterio_key)
print(f"{decrypted_text}")

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