def decripta_e_verificar_mensagem(y, bob_priv_chave, alice_pub_chave):
    """
    Decripta a mensagem, usando a chave privada de Bob e verifica a assinatura
    usando a chave pública de Alice.
    :param y: Mensagem cifrada (assinatura)
    :param bob_priv_chave: Chave privada de Bob (d, n)
    :param alice_pub_chave: Chave pública de Alice (e, n)
    :return: Mensagem original (x)
    """
    d_bob, n_bob = bob_priv_chave
    e_alice, n_alice = alice_pub_chave

    # Bob decifra a mensagem com sua chave privada
    s = pow(y, d_bob, n_bob)

    # Verifica assinatura com a chave pública de Alice
    x = pow(s, e_alice, n_alice)

    return x


if __name__ == "__main__":
    # Dados do problema
    y = 51859
    bob_priv = (57251, 135379)
    alice_pub = (14641, 127273)

    mensagem_original = decripta_e_verificar_mensagem(y, bob_priv, alice_pub)
    print("Texto em claro:", mensagem_original)
