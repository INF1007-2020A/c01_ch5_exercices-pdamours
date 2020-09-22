#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List


def convert_to_absolute() -> float:
    return abs(float(input("Entrez un nombre: ")))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    
    result = []

    for letter in prefixes:
        result.append(letter + suffixes)

    return result


def prime_integer_summation() -> int:
    primes = []
    i = 2
    while len(primes) < 100:
        is_prime = True

        for divider in range(2, int(math.sqrt(i))+ 1):
            if i % divider == 0:
                is_prime = False

        if is_prime:
            primes.append(i)
        
        i += 1

    return sum(primes)


def factorial(number: int) -> int:
    return math.factorial(number)


def use_continue() -> None:
    boucle = []
    for i in range(1, 11):
        if i == 5:
            continue
        else:
            boucle.append(i)

    return print(boucle)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombres premiers est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
