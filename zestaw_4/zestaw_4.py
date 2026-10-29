#!/usr/bin/env python3
# coding=utf-8

"""Zestaw 4 - Milosz Tominski"""

import math


def make_ruler(n: int) -> str:
    """Zadanie 4.2: zwraca miarke o dlugosci n jako napis."""
    if n < 0:
        raise ValueError("dlugosc miarki nie moze byc ujemna")
    bars = "|" + "....|" * n
    numbers = "0" + "".join(f"{i:>5}" for i in range(1, n + 1))
    return bars + "\n" + numbers


def make_grid(rows: int, cols: int) -> str:
    """Zadanie 4.2: zwraca prostokat z kratek rows x cols jako napis."""
    if rows < 0 or cols < 0:
        raise ValueError("liczba wierszy i kolumn nie moze byc ujemna")
    border = "+" + "---+" * cols
    middle = "|" + "   |" * cols
    return "\n".join([border] + [middle, border] * rows)


def factorial(n: int) -> int:
    """Zadanie 4.3: zwraca silnie n! obliczona iteracyjnie."""
    if n < 0:
        raise ValueError("silnia jest okreslona tylko dla n >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Funkcja do zadania 4.4

# Funkcja do zadania 4.5

# Funkcja do zadania 4.6

# Funkcja do zadania 4.7


if __name__ == "__main__":
    # Testy do zadania 4.2
    print(f"Zadanie 4.2, miarka dla n = 12:\n{make_ruler(12)}")
    print(f"Zadanie 4.2, prostokat 2 x 4:\n{make_grid(2, 4)}")
    assert make_ruler(12) == (
        "|....|....|....|....|....|....|....|....|....|....|....|....|\n"
        "0    1    2    3    4    5    6    7    8    9   10   11   12")
    assert make_ruler(0) == "|\n0"
    bars, numbers = make_ruler(150).split("\n")
    for i in range(151):
        assert bars[5 * i] == "|" and numbers[5 * i] == str(i)[-1]
    assert make_grid(2, 4) == (
        "+---+---+---+---+\n"
        "|   |   |   |   |\n"
        "+---+---+---+---+\n"
        "|   |   |   |   |\n"
        "+---+---+---+---+")
    assert make_grid(3, 1) == "+---+\n|   |\n+---+\n|   |\n+---+\n|   |\n+---+"
    assert make_grid(0, 3) == "+---+---+---+"
    for bad_call in (lambda: make_ruler(-1), lambda: make_grid(-1, 2),
                     lambda: make_grid(2, -1)):
        try:
            bad_call()
        except ValueError:
            pass
        else:
            raise AssertionError("brak ValueError dla ujemnego argumentu")

    # Testy do zadania 4.3
    print(f"Zadanie 4.3, 10! = {factorial(10)}")
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    for n in range(50):
        assert factorial(n) == math.factorial(n)
    try:
        factorial(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("brak ValueError dla factorial(-1)")

    # Testy do zadania 4.4

    # Testy do zadania 4.5

    # Testy do zadania 4.6

    # Testy do zadania 4.7
