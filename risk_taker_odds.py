#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#======================================#
#=            RISK TAKER ODDS         =#
#======================================#

"""
    Вычисляет математическое ожидание потерь при атаке.
    Для игры Risk: Global Domination.
"""


import random


battles_amount = 100_000


def roll_dice():
    return random.randint(1, 6)


def run_simulation_3_2():
    losses = {"ATK":0, "DEF":0}
    for _ in range(battles_amount):
        # Battle action
        # 3 atackers vs 2 defenders
        # ATK
        a1 = roll_dice()
        a2 = roll_dice()
        a3 = roll_dice()
        alist = [a1, a2, a3]
        alist.sort(reverse=True)
        # DEF
        d1 = roll_dice()
        d2 = roll_dice()
        dlist = [d1, d2]
        dlist.sort(reverse=True)
        # Results
        if alist[0] > dlist[0]: # in case of tie, defender wins
            losses["DEF"] += 1
        else:
            losses["ATK"] += 1
        if alist[1] > dlist[1]:
            losses["DEF"] += 1
        else:
            losses["ATK"] += 1
    return losses


def run_simulation_2_2():
    losses = {"ATK":0, "DEF":0}
    for _ in range(battles_amount):
        # Battle action
        # 2 atackers vs 2 defenders
        # ATK
        a1 = roll_dice()
        a2 = roll_dice()
        alist = [a1, a2]
        alist.sort(reverse=True)
        # DEF
        d1 = roll_dice()
        d2 = roll_dice()
        dlist = [d1, d2]
        dlist.sort(reverse=True)
        # Results
        if alist[0] > dlist[0]: # in case of tie, defender wins
            losses["DEF"] += 1
        else:
            losses["ATK"] += 1
        if alist[1] > dlist[1]:
            losses["DEF"] += 1
        else:
            losses["ATK"] += 1
    return losses


def run_simulation_3_1():
    losses = {"ATK":0, "DEF":0}
    for _ in range(battles_amount):
        # Battle action
        # 3 atackers vs 1 defender
        # ATK
        a1 = roll_dice()
        a2 = roll_dice()
        a3 = roll_dice()
        alist = [a1, a2, a3]
        alist.sort(reverse=True)
        # DEF
        d1 = roll_dice()
        # Results
        if alist[0] > d1: # in case of tie, defender wins
            losses["DEF"] += 1
        else:
            losses["ATK"] += 1
    return losses


def run_simulation_2_1():
    losses = {"ATK":0, "DEF":0}
    for _ in range(battles_amount):
        # Battle action
        # 2 atackers vs 1 defender
        # ATK
        a1 = roll_dice()
        a2 = roll_dice()
        alist = [a1, a2]
        alist.sort(reverse=True)
        # DEF
        d1 = roll_dice()
        # Results
        if alist[0] > d1: # in case of tie, defender wins
            losses["DEF"] += 1
        else:
            losses["ATK"] += 1
    return losses



#===================== MAIN =====================

def main():
    print("=" * 16 + " Running simulation... " + "=" * 16)
    print("Battles: ", battles_amount)
    losses_3_2 = run_simulation_3_2()
    losses_2_2 = run_simulation_2_2()
    losses_3_1 = run_simulation_3_1()
    losses_2_1 = run_simulation_2_1()
    print("=" * 16 + " Done. " + "=" * 16)

    print("Losses 3 vs 2:", losses_3_2)
    math_val_atk = losses_3_2["ATK"] / battles_amount
    math_val_def = losses_3_2["DEF"] / battles_amount
    print("ATK math val:", math_val_atk)
    print("DEF math val:", math_val_def)

    print("Losses 2 vs 2:", losses_2_2)
    math_val_atk = losses_2_2["ATK"] / battles_amount
    math_val_def = losses_2_2["DEF"] / battles_amount
    print("ATK math val:", math_val_atk)
    print("DEF math val:", math_val_def)

    print("Losses 3 vs 1:", losses_3_1)
    math_val_atk = losses_3_1["ATK"] / battles_amount
    math_val_def = losses_3_1["DEF"] / battles_amount
    print("ATK math val:", math_val_atk)
    print("DEF math val:", math_val_def)

    print("Losses 2 vs 1:", losses_2_1)
    math_val_atk = losses_2_1["ATK"] / battles_amount
    math_val_def = losses_2_1["DEF"] / battles_amount
    print("ATK math val:", math_val_atk)
    print("DEF math val:", math_val_def)


#================================================


if __name__ == "__main__":
    main()
