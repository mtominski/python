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


def total_length(text: str) -> int:
    """Zadanie 2.13: zwraca laczna dlugosc wyrazow w napisie."""
    return sum(len(word) for word in text.split())


def longest_word(text: str) -> str:
    """Zadanie 2.14: zwraca najdluzszy wyraz w napisie."""
    return max(text.split(), key=len, default="")


def longest_word_length(text: str) -> int:
    """Zadanie 2.14: zwraca dlugosc najdluzszego wyrazu w napisie."""
    return len(longest_word(text))


def join_numbers(numbers: list[int]) -> str:
    """Zadanie 2.15: zwraca napis z cyfr kolejnych liczb z listy."""
    return "".join(str(number) for number in numbers)


def replace_gvr(text: str) -> str:
    """Zadanie 2.16: zamienia kazde GvR na Guido van Rossum."""
    return text.replace("GvR", "Guido van Rossum")


# Funkcja do zadania 2.17

# Funkcja do zadania 2.18

# Funkcja do zadania 2.19


if __name__ == "__main__":
    line = ("Python to jezyk programowania\n"
            "stworzony przez GvR\n"
            "w roku 1991")

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
    print(f"Zadanie 2.13, laczna dlugosc wyrazow: {total_length(line)}")
    assert total_length(line) == 52
    assert total_length("") == 0
    assert total_length("jeden \t dwa\n\ntrzy") == 12

    # Testy do zadania 2.14
    print(f"Zadanie 2.14, najdluzszy wyraz: {longest_word(line)}")
    print(f"Zadanie 2.14, jego dlugosc: {longest_word_length(line)}")
    assert longest_word(line) == "programowania"
    assert longest_word_length(line) == 13
    assert longest_word("ala ma kota") == "kota"
    assert longest_word("ab cd") == "ab"
    assert longest_word("") == ""
    assert longest_word_length("") == 0

    # Testy do zadania 2.15
    L = [7, 24, 365, 1, 10]
    print(f"Zadanie 2.15, cyfry liczb z listy: {join_numbers(L)}")
    assert join_numbers(L) == "724365110"
    assert join_numbers([5]) == "5"
    assert join_numbers([]) == ""

    # Testy do zadania 2.16
    print(f"Zadanie 2.16, po zamianie: {replace_gvr(line)}")
    assert "GvR" not in replace_gvr(line)
    assert "przez Guido van Rossum" in replace_gvr(line)
    assert replace_gvr("GvR i GvR") == "Guido van Rossum i Guido van Rossum"
    assert replace_gvr("bez skrotu") == "bez skrotu"
    assert replace_gvr("") == ""

    # Testy do zadania 2.17

    # Testy do zadania 2.18

    # Testy do zadania 2.19