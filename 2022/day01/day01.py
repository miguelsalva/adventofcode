#!/usr/bin/env python3

import sys

INPUT_FILE = "input"
ELVES_LIST = []
CALORIES_NUMBER = 0


def max_list(lista):
  max = 0 
  for x in lista:
    if x > max:
      max = x
  return max


def top_max3_list(lista):
  max1 = 0 
  max2 = 0 
  max3 = 0 
  for x in lista:
    if x > max1:
      max3 = max2
      max2 = max1
      max1 = x
    elif x > max2:
      max3 = max2
      max2 = x
    elif x > max3:
      max3 = x
  return max1 + max2 + max3


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
print(top_max3_list(ELVES_LIST))
