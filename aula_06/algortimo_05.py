def cal_mod(a, n):
    """
    Calcula o módulo de um número inteiro a em relação a n.
    O resultado é sempre um número inteiro no intervalo [0, n-1].
    :param a: Número inteiro
    :param n: Número inteiro positivo
    :return: Módulo de a em relação a n
    """
    return abs(a % n) if a >= 0 else (n - abs(a) % n) % n


if __name__ == '__main__':
    # Python automaticamente ajusta para o intervalo [0, n-1]
    a = -5
    n = 3
    print(f"cal_mod({a}, {n}) = {cal_mod(a, n)}")


    a = 7
    n = 5
    print(f"cal_mod({a}, {n}) = {cal_mod(a, n)}")


    a = -1
    n = 4
    print(f"cal_mod({a}, {n}) = {cal_mod(a, n)}")
