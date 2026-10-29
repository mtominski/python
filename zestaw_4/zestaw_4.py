#!/usr/bin/env python3
# coding=utf-8

"""Zestaw 4 - Milosz Tominski"""

import math
from collections.abc import Sequence


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


def fibonacci(n: int) -> int:
    """Zadanie 4.4: zwraca n-ty wyraz ciagu Fibonacciego (iteracyjnie)."""
    if n < 0:
        raise ValueError("numer wyrazu ciagu musi byc >= 0")
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def odwracanie(L: list, left: int, right: int) -> None:
    """Zadanie 4.5: odwraca w miejscu L od left do right (iteracyjnie)."""
    if not 0 <= left <= right < len(L):
        raise ValueError("niepoprawny zakres left, right")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rek(L: list, left: int, right: int) -> None:
    """Zadanie 4.5: odwraca w miejscu L od left do right (rekurencyjnie)."""
    if not 0 <= left <= right < len(L):
        raise ValueError("niepoprawny zakres left, right")
    L[left], L[right] = L[right], L[left]
    if left + 1 < right - 1:
        odwracanie_rek(L, left + 1, right - 1)


def sum_seq(sequence: Sequence) -> float:
    """Zadanie 4.6: zwraca sume liczb z sekwencji z podsekwencjami."""
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total


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
    first = [fibonacci(n) for n in range(15)]
    print(f"Zadanie 4.4, pierwsze wyrazy: {first}")
    assert first == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    assert fibonacci(50) == 12586269025
    for n in range(2, 100):
        assert fibonacci(n) == fibonacci(n - 1) + fibonacci(n - 2)
    try:
        fibonacci(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("brak ValueError dla fibonacci(-1)")

    # Testy do zadania 4.5
    L = list(range(10))
    odwracanie(L, 2, 6)
    print(f"Zadanie 4.5, po odwracanie(L, 2, 6): {L}")
    assert L == [0, 1, 6, 5, 4, 3, 2, 7, 8, 9]
    for reverse in (odwracanie, odwracanie_rek):
        for left in range(8):
            for right in range(left, 8):
                L = list(range(8))
                expected = list(range(8))
                expected[left:right + 1] = expected[left:right + 1][::-1]
                assert reverse(L, left, right) is None
                assert L == expected
        for left, right in ((5, 2), (-1, 3), (0, 8)):
            try:
                reverse(list(range(8)), left, right)
            except ValueError:
                pass
            else:
                raise AssertionError(f"brak ValueError dla {left}, {right}")

    # Testy do zadania 4.6
    sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print(f"Zadanie 4.6, suma {sequence} = {sum_seq(sequence)}")
    assert sum_seq(sequence) == 45
    assert sum_seq([1, 2, 3]) == 6
    assert sum_seq((1, [2, (3,)])) == 6
    assert sum_seq([[[[[5]]]]]) == 5
    assert sum_seq([1.5, (2.5, [1])]) == 5.0
    assert sum_seq([]) == 0
    assert sum_seq([[], ((), [])]) == 0
    try:
        sum_seq([1, "a"])
    except TypeError:
        pass
    else:
        raise AssertionError("brak TypeError dla elementu nieliczbowego")

    # Testy do zadania 4.7
