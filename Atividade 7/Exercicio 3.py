# Calcule o fatorial de um numero.

def fatorial(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    fat5 = fatorial(5)
    print(fat5)