#!/bin/env/python3

from PIL import Image, ImageDraw
from termcolor import colored

# Tinkoff CTF chall "Men in Black"
# Analyze scrambled pattern and restore image

# 777 (w) x 437 (h)
WIDTH = 777
HEIGHT = 437

PROBE_SCRAMBLED_PATH = "./gradient_neur.png"
TARGET_SCRAMBLED_PATH = "./flashied.png"
RESTORED_PATH = "./restored.png"


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


# Inverse function   r, g, b -> x, y
def translate_inverse(r, g, b):
    x1 = b // 10
    y1 = b % 10
    x2 = r // 10
    x3 = r % 10
    y2 = g // 10
    y3 = g % 10
    x = x1 * 100 + x2 * 10 + x3
    y = y1 * 100 + y2 * 10 + y3
    return (x, y)


def main():
    print("Collecting probe inverse data...")
    probe_image = Image.open(PROBE_SCRAMBLED_PATH)
    pixels = probe_image.load()
    inverse_data = {} # current x,y -> original x,y
    for y in range(HEIGHT):
        for x in range(WIDTH):
            r, g, b = pixels[x, y]
            (orig_x, orig_y) = translate_inverse(r, g, b)
            inverse_data[(x, y)] = (orig_x, orig_y)

    print(f"Restoring image into: {RESTORED_PATH}")
    target_image = Image.open(TARGET_SCRAMBLED_PATH)
    new_image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(new_image)
    pixels = target_image.load()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            r, g, b = pixels[x, y]
            (correct_x, correct_y) = inverse_data[(x, y)]
            draw.point((correct_x, correct_y), fill=(r, g, b))

    new_image.save(RESTORED_PATH)

if __name__ == "__main__":
    main()
