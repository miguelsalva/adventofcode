#!/usr/bin/env python3

import sys

INPUT_FILE = "input.example"


def rucksack_size(linea):
  return len(linea) - 1

file = open(INPUT_FILE, "r")
lines = file.readlines()

for line in lines:
  print(line)
  print(rucksack_size(line))
  print(line[0:rucksack_size(line)//2])
  print(line[rucksack_size(line)//2:])
  #print(line[0:rucksack_size(line)//2].interesection(line[rucksack_size(line)//2:]))
file.close()
