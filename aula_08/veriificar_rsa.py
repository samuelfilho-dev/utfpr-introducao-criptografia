def verificar_rsa(s, e, n, x):
    """
    Verifica se a assinatura s é válida para a mensagem x usando a chave pública (e, n).
    Retorna uma tupla com o resultado da verificação e o resultado da assinatura.
    :param s: Assinatura a ser verificada
    :param e: Expoente da chave pública
    :param n: Módulo da chave pública
    :param x: Mensagem original
    :return: (bool, int) - True se a assinatura for válida, False caso contrário, e o resultado da assinatura.
    """
    ass_valida = pow(s, e, n) == x
    ass_resultado = pow(s, e, n)
    return ass_valida, ass_resultado


def main(s, e, n, x, exe_number):
    """
    Função principal para verificar a assinatura RSA.
    """
    resultado = verificar_rsa(s, e, n, x)
    print("*" * 50, f"Verificar o exercício do RSA {exe_number}", "*" * 50)
    print(f"Resultado da verificação: {resultado[0]}")
    print(f"Resultado da assinatura: {resultado[1]}")


if __name__ == "__main__":
    main(6292, 131, 9797, 123, 1)  # exercício 1
    main(4768, 131, 9797, 4333, 2)  # exercício 2
    main(1424, 131, 9797, 4333, 3)  # exercício 3
