#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: AI (ChatGPT)

import os
import fileinput

def replace_word_in_files(folder_path, old_word, new_word):
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            #if filename == "tags.json":
            #    continue
            file_path = os.path.join(dirpath, filename)
            with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
                for line in file:
                    line = line.replace(old_word, new_word)
                    print(line, end='')

# Specify the folder path, old word, and new word
folder_path = '/Users/Projects/Android/MPAD/data/src/debug/assets'
old_word = 'Фикс'
new_word = 'fixed_time'

# Call the function to replace the word in files
replace_word_in_files(folder_path, old_word, new_word)
