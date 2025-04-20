from math import ceil, sqrt


# Foi usado o algoritmo Baby Step Giant Step para resolver o problema da quebra de chave Diffie-Hellman.
def baby_step_giant_step(g, h, p):
    """
    Resolve g^x = h (mod p) usando o algoritmo Baby Step Giant Step.
    :param g: base
    :param h: valor alvo
    :param p: primo
    :return: x, a solução para g^x = h (mod p)
    """

    # Verifica se g é um gerador
    N = ceil(sqrt(p - 1))

    # Baby Step
    tbl = {pow(g, i, p): i for i in range(N)}

    # Inverso de g^N
    c = pow(g, N * (p - 2), p)

    # Giant Step
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None


if __name__ == '__main__':
    p = 211
    g = 199
    A = 58
    B = 171

    a = baby_step_giant_step(
        p=p,
        g=g,
        h=A,
    )
    b = baby_step_giant_step(
        p=p,
        g=g,
        h=B,
    )

    print(f"Chave privada de Alice (a): {a}")
    print(f"Chave privada de Bob (b): {b}")

    print("=" * 50)
    ## Exercício 2
    p = 6547
    g = 5747
    A = 4571
    B = 2393

    a = baby_step_giant_step(
        p=p,
        g=g,
        h=A,
    )
    b = baby_step_giant_step(
        p=p,
        g=g,
        h=B,
    )

    print(f"Chave privada de Alice (a): {a}")
    print(f"Chave privada de Bob (b): {b}")

    print("=" * 50)
    ## Exercício 3
    p = 12889
    g = 260
    A = 4176
    B = 6598

    a = baby_step_giant_step(
        p=p,
        g=g,
        h=A,
    )
    b = baby_step_giant_step(
        p=p,
        g=g,
        h=B,
    )

    print(f"Chave privada de Alice (a): {a}")
    print(f"Chave privada de Bob (b): {b}")
