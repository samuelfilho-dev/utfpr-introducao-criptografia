import time
import psutil


def mod_for_exp_naive(q, x, n):
    """
    Naive implementation of modular exponentiation.
    This function computes q^x mod n using a simple loop.
    It is not efficient for large values of x.
    :param q: Base
    :param x: Exponent
    :param n: Modulus
    :return: Result of q^x mod n
    """
    result = 1
    for _ in range(x):
        result = (result * q) % n
    return result


def mod_for_exp_square_mult(q, x, n):
    """
    Square-and-Multiply implementation of modular exponentiation.
    This function computes q^x mod n using the square-and-multiply method.
    It is more efficient than the naive method for large values of x.
    :param q: Base
    :param x: Exponent
    :param n: Modulus
    :return: Result of q^x mod n
    """
    result = 1
    q = q % n
    while x > 0:
        if x % 2 == 1:
            result = (result * q) % n
        q = (q * q) % n
        x //= 2
    return result


def mod_for_exp_improved(q, x, n):
    """
    Improved implementation of modular exponentiation.
    This function computes q^x mod n using a more efficient method.
    It reduces the base q modulo n before starting the exponentiation.
    :param q: Base
    :param x: Exponent
    :param n: Modulus
    :return: Result of q^x mod n
    """
    q = q % n
    result = 1
    for _ in range(x):
        result = (result * q) % n
    return result


def time_metric(func, q, x, n):
    start = time.time()
    cpu_start = psutil.cpu_percent(interval=None)
    ram_start = psutil.virtual_memory().percent

    y = func(q, x, n)

    cpu_end = psutil.cpu_percent(interval=None)
    ram_end = psutil.virtual_memory().percent
    end = time.time()

    return y, abs((end - start)), abs((cpu_end - cpu_start)), abs((ram_end - ram_start))


if __name__ == '__main__':
    q = 5
    x = 6
    n = 23

    y_naive, t_naive, cpu_naive, ram_naive = time_metric(mod_for_exp_naive, q, x, n)
    y_improved, t_improved, cpu_improved, ram_improved = time_metric(mod_for_exp_improved, q, x, n)
    y_sqmult, t_sqmult, cpu_sqmult, ram_sqmult = time_metric(mod_for_exp_square_mult, q, x, n)

    print(
        f"Naive:     y = {y_naive}, tempo = {t_naive} segundos, CPU = {cpu_naive:.2f}%, RAM = {ram_naive:.2f}%")
    print(
        f"Improved:  y = {y_improved}, tempo = {t_improved} segundos, CPU = {cpu_improved:.2f}%, RAM = {ram_improved:.2f}%")
    print(
        f"Square-Mult: y = {y_sqmult}, tempo = {t_sqmult} segundos, CPU = {cpu_sqmult:.2f}%, RAM = {ram_sqmult:.2f}%")

    print("=" * 50)
    # Execicio 2
    q = 5
    x = 15
    n = 24

    y_naive, t_naive, cpu_naive, ram_naive = time_metric(mod_for_exp_naive, q, x, n)
    y_improved, t_improved, cpu_improved, ram_improved = time_metric(mod_for_exp_improved, q, x, n)
    y_sqmult, t_sqmult, cpu_sqmult, ram_sqmult = time_metric(mod_for_exp_square_mult, q, x, n)

    print(
        f"Naive:     y = {y_naive}, tempo = {t_naive} segundos, CPU = {cpu_naive:.2f}%, RAM = {ram_naive:.2f}%")
    print(
        f"Improved:  y = {y_improved}, tempo = {t_improved} segundos, CPU = {cpu_improved:.2f}%, RAM = {ram_improved:.2f}%")
    print(
        f"Square-Mult: y = {y_sqmult}, tempo = {t_sqmult} segundos, CPU = {cpu_sqmult:.2f}%, RAM = {ram_sqmult:.2f}%")

    print("=" * 50)
    # Execicio 3
    q = 5
    x = 36
    n = 97

    y_naive, t_naive, cpu_naive, ram_naive = time_metric(mod_for_exp_naive, q, x, n)
    y_improved, t_improved, cpu_improved, ram_improved = time_metric(mod_for_exp_improved, q, x, n)
    y_sqmult, t_sqmult, cpu_sqmult, ram_sqmult = time_metric(mod_for_exp_square_mult, q, x, n)

    print(
        f"Naive:     y = {y_naive}, tempo = {t_naive} segundos, CPU = {cpu_naive:.2f}%, RAM = {ram_naive:.2f}%")
    print(
        f"Improved:  y = {y_improved}, tempo = {t_improved} segundos, CPU = {cpu_improved:.2f}%, RAM = {ram_improved:.2f}%")
    print(
        f"Square-Mult: y = {y_sqmult}, tempo = {t_sqmult} segundos, CPU = {cpu_sqmult:.2f}%, RAM = {ram_sqmult:.2f}%")

    print("=" * 50)
    # Execicio 4
    q = 5
    x = 58
    n = 97

    y_naive, t_naive, cpu_naive, ram_naive = time_metric(mod_for_exp_naive, q, x, n)
    y_improved, t_improved, cpu_improved, ram_improved = time_metric(mod_for_exp_improved, q, x, n)
    y_sqmult, t_sqmult, cpu_sqmult, ram_sqmult = time_metric(mod_for_exp_square_mult, q, x, n)

    print(
        f"Naive:     y = {y_naive}, tempo = {t_naive} segundos, CPU = {cpu_naive:.2f}%, RAM = {ram_naive:.2f}%")
    print(
        f"Improved:  y = {y_improved}, tempo = {t_improved} segundos, CPU = {cpu_improved:.2f}%, RAM = {ram_improved:.2f}%")
    print(
        f"Square-Mult: y = {y_sqmult}, tempo = {t_sqmult} segundos, CPU = {cpu_sqmult:.2f}%, RAM = {ram_sqmult:.2f}%")

    print("=" * 50)
    # Execicio 5
    q = 98
    x = 1000000
    n = 65

    y_naive, t_naive, cpu_naive, ram_naive = time_metric(mod_for_exp_naive, q, x, n)
    y_improved, t_improved, cpu_improved, ram_improved = time_metric(mod_for_exp_improved, q, x, n)
    y_sqmult, t_sqmult, cpu_sqmult, ram_sqmult = time_metric(mod_for_exp_square_mult, q, x, n)

    print(
        f"Naive:     y = {y_naive}, tempo = {t_naive} segundos, CPU = {cpu_naive:.2f}%, RAM = {ram_naive:.2f}%")
    print(
        f"Improved:  y = {y_improved}, tempo = {t_improved} segundos, CPU = {cpu_improved:.2f}%, RAM = {ram_improved:.2f}%")
    print(
        f"Square-Mult: y = {y_sqmult}, tempo = {t_sqmult} segundos, CPU = {cpu_sqmult:.2f}%, RAM = {ram_sqmult:.2f}%")
