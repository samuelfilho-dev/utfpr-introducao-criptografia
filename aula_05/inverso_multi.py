def gf_mul(a, b):
    result = 0
    for i in range(8):
        if b & 1:
            result ^= a
        high_bit = a & 0x80
        a <<= 1
        if high_bit:
            a ^= 0x11B
        b >>= 1
    return result & 0xFF    

def gf_inverse(a):
    if a == 0:
        return 0  # 0 não tem inverso
    for i in range(1, 256):
        if gf_mul(a, i) == 1:
            return i
    return None

# Exemplo:
entrada = 0x75 # Samuel
inverso = gf_inverse(entrada)
print(f"Inverso multiplicativo de {hex(entrada)} é {int(inverso)}")
