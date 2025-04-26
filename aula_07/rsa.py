def extended_euclidean_algorithm(a, b):
    """
    Algoritimo de Euclides estendido para encontrar o máximo divisor comum (MDC) e os coeficientes de Bézout.
    Retorna o MDC e os coeficientes x e y tais que ax + by = gcd(a, b).
    :param a: Primeiro número inteiro
    :param b: Segundo número inteiro
    :return: Tupla (gcd, x, y) onde gcd é o máximo divisor comum e x e y são os coeficientes de Bézout
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    """
    Calcula o inverso modular de a módulo m usando o algoritmo de Euclides estendido.
    O inverso modular é o número x tal que (a * x) % m = 1.
    :param a: Número inteiro para o qual queremos encontrar o inverso modular
    :param m: Módulo
    :return: O inverso modular de a módulo m
    :raises ValueError: Se o inverso não existir (ou seja, se a e m não forem coprimos)
    """
    gcd, x, _ = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % m


def generate_keypair(p, q, e):
    """
    Gera um par de chaves RSA (chave pública e chave privada) usando dois números primos p e q.
    :param p: Primeiro número primo
    :param q: Segundo número primo
    :param e: Expoente público (deve ser coprimo com (p-1)*(q-1))
    :return: Tupla (chave pública, chave privada)
    :raises ValueError: Se e não for coprimo com (p-1)*(q-1)
    """
    n = p * q
    phi = (p - 1) * (q - 1)

    # Verifica se e é coprimo com phi
    if extended_euclidean_algorithm(e, phi)[0] != 1:
        raise ValueError("e and phi(n) are not coprime")

    d = mod_inverse(e, phi)

    return (e, n), (d, n)


def encrypt(public_key, plaintext):
    """
    Criptografa uma mensagem usando a chave pública.
    :param public_key: Chave pública (e, n)
    :param plaintext: Mensagem a ser criptografada (número inteiro)
    :return: Mensagem criptografada (número inteiro)
    """
    e, n = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext


def decrypt(private_key, ciphertext):
    """
    Descriptografa uma mensagem usando a chave privada.
    :param private_key: Chave privada (d, n)
    :param ciphertext: Mensagem criptografada (número inteiro)
    :return: Mensagem original (número inteiro)
    """
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext


def main(p, q, e, mensagem):
    """
    Função principal para executar o algoritmo RSA.
    :param p: Primeiro número primo
    :param q: Segundo número primo
    :param e: Expoente público
    :param mensagem: Mensagem a ser criptografada (número inteiro)
    """
    public_key, private_key = generate_keypair(p, q, e)

    # Criptografar a mensagem
    cypher_text = encrypt(public_key, mensagem)

    # Descriptografar a mensagem
    decrypted_message = decrypt(private_key, cypher_text)

    print("*" * 50)
    print(f"Chave pública: {public_key}")
    print(f"Chave privada: {private_key}")
    print(f"Mensagem original: {mensagem}")
    print(f"Mensagem criptografada: {cypher_text}")
    print(f"Mensagem descriptografada: {decrypted_message}")


if __name__ == "__main__":
    main(p=11, q=13, e=7, mensagem=9)
    main(p=7, q=19, e=5, mensagem=6)
    main(p=17, q=11, e=7, mensagem=88)
