import aleatorio

def generate_key(length):
    return [aleatorio.aleatorio() % 26 for _ in range(length)]

def clear_text(text):
     return ''.join(filter(str.isalpha, text.lower()))

def xor_cypher(text, key):
     return ''.join(chr(((ord(char) - ord('a')) ^ key) + ord('a')) for char, key in zip(text, key))

def main():
     with open ('./aula_03/cifra_xor_a.txt', 'r') as file:
          text = clear_text(file.read())

     keystream = generate_key(len(text))
     cypher_text = xor_cypher(text, keystream)
     print(f'Cypher text \n {cypher_text}')

     print('-' * 50)

     plain_text = xor_cypher(cypher_text, keystream)
     print(f'Plain Text: \n {plain_text}')

if __name__ == '__main__':
     main()
        
