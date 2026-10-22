#!/usr/bin/env python3
# coding=utf-8

"""Zestaw 3 - Milosz Tominski"""


def skip_multiples_of_3_for(limit: int = 30) -> list[int]:
    """Zadanie 3.3: liczby od 0 do limit bez podzielnych przez 3 (for)."""
    result = []
    for number in range(limit + 1):
        if number % 3 != 0:
            result.append(number)
    return result


def skip_multiples_of_3_while(limit: int = 30) -> list[int]:
    """Zadanie 3.3: liczby od 0 do limit bez podzielnych przez 3 (while)."""
    result = []
    number = 0
    while number <= limit:
        if number % 3 != 0:
            result.append(number)
        number += 1
    return result


# Funkcja do zadania 3.4

# Funkcja do zadania 3.5

# Funkcja do zadania 3.6

# Funkcja do zadania 3.8

# Funkcja do zadania 3.9

# Funkcja do zadania 3.10


if __name__ == "__main__":
    # Testy do zadania 3.3
    print(f"Zadanie 3.3, petla for: {skip_multiples_of_3_for()}")
    print(f"Zadanie 3.3, petla while: {skip_multiples_of_3_while()}")
    expected = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14,
                16, 17, 19, 20, 22, 23, 25, 26, 28, 29]
    assert skip_multiples_of_3_for() == expected
    assert skip_multiples_of_3_while() == expected
    for limit in range(10):
        assert (skip_multiples_of_3_for(limit)
                == skip_multiples_of_3_while(limit))
    assert skip_multiples_of_3_for(0) == []
    assert skip_multiples_of_3_for(3) == [1, 2]

    # Testy do zadania 3.4

    # Testy do zadania 3.5

    # Testy do zadania 3.6

    # Testy do zadania 3.8

    # Testy do zadania 3.9

    # Testy do zadania 3.10
