from rsa import mod_inverse


def factor_n(n):
    """
    Fatora o número n em dois números primos p e q.
    :param n: Número a ser fatorado
    :return: Tupla (p, q) onde p e q são os fatores primos de n
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    raise ValueError("n não é um produto de dois primos conhecidos")


def crack_rsa(y, e, n):
    """
    Quebra o RSA dado o valor cifrado y, o expoente público e e o módulo n.
    :param y: Valor cifrado
    :param e: Expoente público
    :param n: Módulo
    :return: Mensagem decifrada
    """
    p, q = factor_n(n)
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    m = pow(y, d, n)
    return m


def main(y, e, n, exe_number):
    """
    Função principal para executar o código de quebra do RSA.
    :param y: Valor cifrado
    :param e: Expoente público
    :param n: Módulo
    """
    x = crack_rsa(y, e, n)
    print("*" * 25, "EXERCÍCIO", exe_number, "*" * 25)
    print(f"Mensagem decifrada: {x}")


if __name__ == "__main__":
    main(
        y=1141,
        e=2111,
        n=2623,
        exe_number=1,
    )

    main(y=1632643, e=5, n=6326693, exe_number=2)
