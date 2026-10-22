#!/usr/bin/env python3
# coding=utf-8

"""Zestaw 3 - Milosz Tominski"""

from collections.abc import Sequence


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


def cube_message(text: str) -> str:
    """Zadanie 3.4: zwraca x i x**3 albo komunikat o bledzie."""
    try:
        x = float(text)
    except ValueError:
        return f"Blad: {text!r} nie jest liczba"
    else:
        return f"x = {x}, x**3 = {x ** 3}"


def cube_loop() -> None:
    """Zadanie 3.4: wczytuje liczby w petli az do wpisania stop."""
    while True:
        try:
            text = input("Podaj liczbe (stop konczy): ")
        except EOFError:
            print()
            break
        if text.strip() == "stop":
            break
        print(cube_message(text))


def make_ruler(length: int) -> str:
    """Zadanie 3.5: zwraca miarke o zadanej dlugosci jako napis."""
    bars = "|" + "....|" * length
    numbers = "0" + "".join(f"{i:>5}" for i in range(1, length + 1))
    return bars + "\n" + numbers


def make_grid(columns: int, rows: int) -> str:
    """Zadanie 3.6: zwraca prostokat z kratek jako napis."""
    border = "+" + "---+" * columns
    middle = "|" + "   |" * columns
    return "\n".join([border] + [middle, border] * rows)


def common_elements(first: Sequence, second: Sequence) -> list:
    """Zadanie 3.8a: zwraca elementy wspolne obu sekwencji bez powtorzen."""
    return sorted(set(first) & set(second))


def all_elements(first: Sequence, second: Sequence) -> list:
    """Zadanie 3.8b: zwraca wszystkie elementy obu sekwencji bez powtorzen."""
    return sorted(set(first) | set(second))


def sequence_sums(sequences: Sequence[Sequence[float]]) -> list[float]:
    """Zadanie 3.9: zwraca liste sum liczb z kolejnych sekwencji."""
    return [sum(sequence) for sequence in sequences]


def roman_dict_literal() -> dict[str, int]:
    """Zadanie 3.10: slownik cyfr rzymskich zapisany jako literal."""
    return {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_dict_keywords() -> dict[str, int]:
    """Zadanie 3.10: slownik cyfr rzymskich z dict() i nazwanych argumentow."""
    return dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def roman_dict_zip() -> dict[str, int]:
    """Zadanie 3.10: slownik cyfr rzymskich z dict() i zip()."""
    return dict(zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000]))


def roman_dict_pairs() -> dict[str, int]:
    """Zadanie 3.10: slownik cyfr rzymskich z listy par (klucz, wartosc)."""
    pairs = [("I", 1), ("V", 5), ("X", 10), ("L", 50),
             ("C", 100), ("D", 500), ("M", 1000)]
    return dict(pairs)


def roman_dict_comprehension() -> dict[str, int]:
    """Zadanie 3.10: slownik skladany wyliczany ze wzoru 1, 5, 10, 50..."""
    return {digit: (5 if i % 2 else 1) * 10 ** (i // 2)
            for i, digit in enumerate("IVXLCDM")}


def roman_dict_loop() -> dict[str, int]:
    """Zadanie 3.10: slownik cyfr rzymskich wypelniany w petli for."""
    result = {}
    for digit, value in zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000]):
        result[digit] = value
    return result


def roman2int(text: str) -> int:
    """Zadanie 3.10: zamienia liczbe zapisana po rzymsku na arabska."""
    digits = roman_dict_literal()
    values = []
    for letter in text:
        if letter not in digits:
            raise ValueError(f"niepoprawna cyfra rzymska: {letter!r}")
        values.append(digits[letter])
    total = 0
    for value, next_value in zip(values, values[1:] + [0]):
        if value < next_value:
            total -= value
        else:
            total += value
    return total


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
    print(f"Zadanie 3.4, dla 2: {cube_message('2')}")
    print(f"Zadanie 3.4, dla abc: {cube_message('abc')}")
    assert cube_message("2") == "x = 2.0, x**3 = 8.0"
    assert cube_message("-1.5") == "x = -1.5, x**3 = -3.375"
    assert cube_message(" 3 ") == "x = 3.0, x**3 = 27.0"
    assert cube_message("abc") == "Blad: 'abc' nie jest liczba"
    assert cube_message("") == "Blad: '' nie jest liczba"

    # Testy do zadania 3.5
    x = 12
    print(f"Zadanie 3.5, miarka dla x = {x}:\n{make_ruler(x)}")
    assert make_ruler(x) == (
        "|....|....|....|....|....|....|....|....|....|....|....|....|\n"
        "0    1    2    3    4    5    6    7    8    9   10   11   12")
    assert make_ruler(0) == "|\n0"
    assert make_ruler(1) == "|....|\n0    1"
    bars, numbers = make_ruler(150).split("\n")
    for i in range(151):
        assert bars[5 * i] == "|" and numbers[5 * i] == str(i)[-1]

    # Testy do zadania 3.6
    x = 4
    y = 2
    print(f"Zadanie 3.6, prostokat dla x = {x}, y = {y}:\n{make_grid(x, y)}")
    assert make_grid(x, y) == (
        "+---+---+---+---+\n"
        "|   |   |   |   |\n"
        "+---+---+---+---+\n"
        "|   |   |   |   |\n"
        "+---+---+---+---+")
    assert make_grid(1, 1) == "+---+\n|   |\n+---+"
    assert make_grid(3, 0) == "+---+---+---+"
    assert make_grid(2, 3).count("\n") == 6

    # Testy do zadania 3.8
    first = [1, 2, 3, 3, 4]
    second = (3, 4, 4, 5)
    print(f"Zadanie 3.8a, wspolne: {common_elements(first, second)}")
    print(f"Zadanie 3.8b, wszystkie: {all_elements(first, second)}")
    assert common_elements(first, second) == [3, 4]
    assert all_elements(first, second) == [1, 2, 3, 4, 5]
    assert common_elements("abca", "cad") == ["a", "c"]
    assert all_elements("abca", "cad") == ["a", "b", "c", "d"]
    assert common_elements([1, 2], [3, 4]) == []
    assert all_elements([], []) == []

    # Testy do zadania 3.9
    sequences = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
    print(f"Zadanie 3.9, sumy: {sequence_sums(sequences)}")
    assert sequence_sums(sequences) == [0, 4, 3, 7, 18]
    assert sequence_sums([(1.5, 2.5), [-1, 1]]) == [4.0, 0]
    assert sequence_sums([]) == []

    # Testy do zadania 3.10
    roman = roman_dict_literal()
    print(f"Zadanie 3.10, slownik: {roman}")
    assert "".join(roman) == "IVXLCDM"
    assert list(roman.values()) == [1, 5, 10, 50, 100, 500, 1000]
    for build in (roman_dict_keywords, roman_dict_zip, roman_dict_pairs,
                  roman_dict_comprehension, roman_dict_loop):
        assert build() == roman
    print(f"Zadanie 3.10, MCMXCIV = {roman2int('MCMXCIV')}")
    assert roman2int("MCMXCIV") == 1994
    assert roman2int("MMXXVI") == 2026
    assert roman2int("CDXLIV") == 444
    assert roman2int("MMMCMXCIX") == 3999
    first_ten = "I II III IV V VI VII VIII IX X".split()
    assert [roman2int(number) for number in first_ten] == list(range(1, 11))
    assert roman2int("") == 0
    try:
        roman2int("XIA")
    except ValueError as error:
        assert str(error) == "niepoprawna cyfra rzymska: 'A'"
    else:
        raise AssertionError("roman2int nie zglosil ValueError")

    # Program do zadania 3.4
    print("\nZadanie 3.4, program wypisuje x i x**3 dla podanych liczb.\n"
          "Wpisz stop, aby zakonczyc.")
    cube_loop()
