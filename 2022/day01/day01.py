#!/usr/bin/env python3
  2
  3 import sys
  4
  5 INPUT_FILE = "input"
  6 ELVES_LIST = [0]
  7 CALORIES_NUMBER = 0
  8
  9
 10 def max_list(lista):
 11   max = lista[0]
 12   for x in lista:
 13     if x > max:
 14       max = x
 15   return max
 16
 17
 18 file = open(INPUT_FILE, "r")
 19 lines = file.readlines()
 20
 21 for line in lines:
 22   if line != '\n':
 23     CALORIES_NUMBER = CALORIES_NUMBER + int(line)
 24   else:
 25     ELVES_LIST.append(CALORIES_NUMBER)
 26     CALORIES_NUMBER = 0
 27
 28 file.close()
 29
 30 print(max_list(ELVES_LIST))
