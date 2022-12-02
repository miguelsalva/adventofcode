#!/usr/bin/env python3

import sys

INPUT_FILE = "input"
TOTAL_SCORE = 0


def winner (linea):
# The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
  if linea[0] == "A":
    if linea[2] == "X": 
      return 3
    elif linea[2] == "Y":
      return 6
    else:
      return 0
  elif linea [0] == "B":
    if linea[2] == "X":
      return 0
    elif linea[2] == "Y":
      return 3
    else:
      return 6
  else:
    if linea[2] == "X":
      return 6
    elif linea[2] == "Y":
      return 0
    else:
      return 3


def play(linea):
# 1 for Rock, 2 for Paper, and 3 for Scissors
  if linea[2] == "X":
    return 1
  elif linea[2] == "Y":
    return 2
  else:
    return 3 


file = open(INPUT_FILE, "r")
lines = file.readlines()

for line in lines:
  TOTAL_SCORE = TOTAL_SCORE + winner(line) + play(line)
       

file.close()
print(TOTAL_SCORE)
