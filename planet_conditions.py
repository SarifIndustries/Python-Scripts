#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#======================================#
#=         PLANET CONDITIONS          =#
#======================================#

"""
    Выбирает случайное количество и случайные настройки для игры
    в соответствии с весовыми коэффициентами вероятностей.
    Для игры Dome Keeper.
"""

import random
import functools


# Количество случайных настроек
AMOUNTS = [
#   Количество             Вероятность
    (0,                    4),
    (1,                    4),
    (2,                    3),
    (3,                    2),
    (4,                    1),
]

# Настройки планеты
PLANET_CONDITIONS = [
#   Настройка              Вероятность
    ("Feeble enemies",     2),
    ("Long cycles",        3),
    ("Double iron",        1),
    ("Maze structure",     4),
]


"""
    Выбор элемента в соответствии с его весом.
"""
def weighted_choice(settings: list):
    total_weight = functools.reduce(lambda a, b: a+b, [w for (s, w) in settings])
    r = random.random() * total_weight
    # Секции делят интервал (от 0 до Суммы весов) на отрезки для каждого элемента.
    # Проверяем в какую секцию попало случайное число r.
    choice = None
    section = 0
    for (s, w) in settings:
        section += w
        if r < section:
            # Попали в секцию для этого элемента.
            choice = s
            break
    return choice


# Unit test
def test_weighted_choice():
    stats = {0:0, 1:0, 2:0, 3:0, 4:0}
    test_range = 10_000
    for i in range(test_range):
        choice = weighted_choice(AMOUNTS)
        stats[choice] += 1
    percented_stats = {key: f"{int(stats[key] / test_range * 100)} %" for key in stats.keys() }
    print(f"Probability distribution test results:\n{percented_stats}")


#===================== MAIN =====================

def main():
    print("=" * 16 + " Testing probabilities " + "=" * 16)
    test_weighted_choice()
    print()
    print("=" * 16 + " Detecting planet conditions " + "=" * 10)
    amount = weighted_choice(AMOUNTS)
    print(f"Amount of planet conditions: {amount}")
    result = []
    for i in range(amount):
        while True:
            choice = weighted_choice(PLANET_CONDITIONS)
            if choice not in result:
                result.append(choice)
                break
    if amount == 0:
        print("No planet conditions.")
    else:
        print("\t+ " + "\n\t+ ".join(result))
    print()

#================================================


if __name__ == "__main__":
    main()
