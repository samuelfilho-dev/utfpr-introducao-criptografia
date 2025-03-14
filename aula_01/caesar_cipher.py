import sys


def caesar_cipher(text, shift, mode="enc"):
    result = ""
    alphabet_size = 26

    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            shift_value = shift if mode == "enc" else -shift
            result += chr((ord(ch) - base + shift_value) % alphabet_size + base)
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            shift_value = shift if mode == "enc" else -shift
            result += chr((ord(ch) - base + shift_value) % alphabet_size + base)
        else:
            result += ch

    return result


def main():
    if len(sys.argv) < 5:
        print(f"Uso: {sys.argv[0]} input.txt output.txt enc/dec shift")
        sys.exit(1)

    input_file = sys.argv[1] # carta.txt
    output_file = sys.argv[2] # output.txt
    mode = sys.argv[3] # enc
    shift = int(sys.argv[4]) # -3

    with open(input_file, "r", encoding="utf-8") as crypter_file:
        text = crypter_file.read()

    result = caesar_cipher(text, shift, mode)

    with open(output_file, "w", encoding="utf-8") as plain_file:
        plain_file.write(result)

    print(f"Processo concluído! Saída salva em {output_file}")


if __name__ == "__main__":
    main()
