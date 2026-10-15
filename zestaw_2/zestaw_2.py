#!/usr/bin/env python3
# coding=utf-8

"""Zestaw 2 - Milosz Tominski"""


def count_words(text: str) -> int:
    """Zadanie 2.10: zwraca liczbe wyrazow w napisie."""
    return len(text.split())


def split_with_underscore(text: str) -> str:
    """Zadanie 2.11: zwraca znaki napisu rozdzielone znakiem _."""
    return "_".join(text)


def first_chars(text: str) -> str:
    """Zadanie 2.12: zwraca napis z pierwszych znakow wyrazow."""
    return "".join(word[0] for word in text.split())


def last_chars(text: str) -> str:
    """Zadanie 2.12: zwraca napis z ostatnich znakow wyrazow."""
    return "".join(word[-1] for word in text.split())


# Funkcja do zadania 2.13

# Funkcja do zadania 2.14

# Funkcja do zadania 2.15

# Funkcja do zadania 2.16

# Funkcja do zadania 2.17

# Funkcja do zadania 2.18

# Funkcja do zadania 2.19


if __name__ == "__main__":
    line = """Python to jezyk programowania
    stworzony przez GvR
    w roku 1991"""

    # Testy do zadania 2.10
    print(f"Zadanie 2.10, liczba wyrazow: {count_words(line)}")
    assert count_words(line) == 10
    assert count_words("") == 0
    assert count_words("jeden \t dwa\n\ntrzy") == 3

    # Testy do zadania 2.11
    word = "Python"
    print(f"Zadanie 2.11, z podkresleniami: {split_with_underscore(word)}")
    assert split_with_underscore(word) == "P_y_t_h_o_n"
    assert split_with_underscore("a") == "a"
    assert split_with_underscore("") == ""

    # Testy do zadania 2.12
    print(f"Zadanie 2.12, pierwsze znaki: {first_chars(line)}")
    print(f"Zadanie 2.12, ostatnie znaki: {last_chars(line)}")
    assert first_chars(line) == "PtjpspGwr1"
    assert last_chars(line) == "nokayzRwu1"
    assert first_chars("a") == last_chars("a") == "a"
    assert first_chars("") == last_chars("") == ""

    # Testy do zadania 2.13

    # Testy do zadania 2.14

    # Testy do zadania 2.15

    # Testy do zadania 2.16

    # Testy do zadania 2.17

    # Testy do zadania 2.18

    # Testy do zadania 2.19