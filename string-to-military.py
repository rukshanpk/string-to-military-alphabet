#!/usr/bin/env python

import sys

codes = {
    'a': "Alpha",
    'b': "Bravo",
    'c': "Charlie",
    'd': "Delta",
    'e': "Echo",
    'f': "Foxtrot",
    'g': "Golf",
    'h': "Hotel",
    'i': "India",
    'j': "Juliet",
    'k': "Kilo",
    'l': "Lima",
    'm': "Mike",
    'n': "November",
    'o': "Oscar",
    'p': "Papa",
    'q': "Quebec",
    'r': "Romeo",
    's': "Sierra",
    't': "Tango",
    'u': "Uniform",
    'v': "Victor",
    'w': "Whisky",
    'x': "XRay",
    'y': "Yankee",
    'z': "Zulu",
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "nine"
}

while True:
    word = raw_input("String to convert : ")
    print("\n")
    if word == "":
        exit()
    for letter in word.lower():
        if letter in codes:
            print(letter.upper()+"-for-"+codes[letter])
