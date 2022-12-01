#!/usr/bin/env python3

import sys

INPUT_FILE = "input"
ELVES_LIST = [0]
CALORIES_NUMBER = 0


def max_list(lista):
  max = lista[0]
  for x in lista:
    if x > max:
      max = x
  return max


file = open(INPUT_FILE, "r")
lines = file.readlines()

for line in lines:
  if line != '\n':
    CALORIES_NUMBER = CALORIES_NUMBER + int(line)
  else:
    ELVES_LIST.append(CALORIES_NUMBER)
    CALORIES_NUMBER = 0

file.close()

print(max_list(ELVES_LIST))
