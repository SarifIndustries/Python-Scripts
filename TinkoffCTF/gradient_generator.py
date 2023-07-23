#!/bin/env/python3

from PIL import Image, ImageDraw
from termcolor import colored

# Tinkoff CTF chall "Men in Black"
# Generates gradient probe image with unique pixel colors

# 777 (w) x 437 (h)
WIDTH = 777
HEIGHT = 437

PATH = "./gradient.png"

def return_caret():
    print("\033[0G", end='', flush=True)


def progress(percent):
    p = int(percent)
    return_caret()
    print(colored(f"{p} %", color="light_green"), end='')


# x < 1000; y < 1000;   x, y -> r, g, b
def translate_alt(x, y):
    c = x * 1000 + y
    r = c % 100
    g = c % 10_000 // 100
    b = c // 10_000
    return (r, g, b)


# x < 1000; y < 1000;   x, y -> r, g, b
def translate(x, y):
    x1 = x // 100
    x2 = x % 100 // 10
    x3 = x % 10
    y1 = y // 100
    y2 = y % 100 // 10
    y3 = y % 10
    r = x2 * 10 + x3
    g = y2 * 10 + y3
    b = x1 * 10 + y1
    return (r, g, b)


def verify_uniq(image):
    print("Verifying image...")
    width, height = image.size
    pixels = image.load()
    colors = []
    progress(0)
    for y in range(height):
        for x in range(width):
            color = pixels[x, y]
            if color in colors:
                print(colored("Color is not unique!", color="red"))
            colors.append(color)
        progress(y * 100 / height)
    progress(100)
    print()


def main():
    print("Generating gradient image...")

    new_image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(new_image)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = translate(x, y)
            draw.point((x, y), fill=color)

    new_image.save(PATH)
    verify_uniq(new_image)
    

if __name__ == "__main__":
    main()
