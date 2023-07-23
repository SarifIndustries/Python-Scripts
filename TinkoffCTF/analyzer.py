#!/bin/env/python3

from PIL import Image
from termcolor import colored

# Tinkoff CTF chall "Men in Black"
# Compares pixel count in both images

# 777 (w) x 437 (h)
WIDTH = 777
HEIGHT = 437

PATH_1 = "./circle_neur.png"
PATH_2 = "./circle.png"


def return_caret():
    print("\033[0G", end='', flush=True)


def progress(percent):
    p = int(percent)
    return_caret()
    print(colored(f"{p} %", color="light_green"), end='')


def verify_size(image):
    width, height = image.size
    print(f"width: {width}", f"height: {height}")
    print("Total pixel count: " + str(height * width))
    if width != WIDTH or height != HEIGHT:
        print("Wrong width and height.")
        exit(0)
    else:
        print("Size match.")
    

def count_white_red_black(image):
    width, height = image.size
    pixels = image.load()
    white = 0
    red = 0
    black = 0
    unknown = 0
    print("Counting pixel colors...")
    progress(0)
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if r == 0 and g == 0 and b == 0:
                black += 1
                continue
            if r == 255 and g == 255 and b == 255:
                white += 1
                continue
            if r == 255 and g == 0 and b == 0:
                red += 1
                continue
            unknown += 1
        progress(y * 100 / height)
    if unknown != 0:
        print(colored(f"Unknown pixels: {unknown}", color="red"))
    progress(100)
    print()
    return (white, red, black)


def main():
    print("File: " + colored(PATH_1, color="cyan"))
    image = Image.open(PATH_1)
    verify_size(image)
    (white_1, red_1, black_1) = count_white_red_black(image)
    print(f"white: {white_1}   red: {red_1}   black: {black_1}")

    print()

    image = Image.open(PATH_2)
    verify_size(image)
    (white_2, red_2, black_2) = count_white_red_black(image)
    print(f"white: {white_1}   red: {red_1}   black: {black_1}")

    if white_1 == white_2 and red_1 == red_2 and black_1 == black_2:
        print(colored("Colors count match!", color="light_magenta"))

if __name__ == "__main__":
    main()
