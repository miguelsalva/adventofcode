#!/usr/bin/env python3

import sys

INPUT_FILE = "input"
PRIORITY_VALUES = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
SUM_PRIORITIES = 0


def rucksack_size(linea):
  return len(linea) - 1


def common_items(list1,list2):
  return (set(list1).intersection(list2))


def get_priority(common_list):
  return PRIORITY_VALUES.rfind(common_list[0])


file = open(INPUT_FILE, "r")
lines = file.readlines()

for line in lines:
  part1 = line[0:rucksack_size(line)//2]
  part2 = line[rucksack_size(line)//2:]
  COMMON = common_items(part1,part2)
  COMMON_STRING = ' '.join(map(str, COMMON))
  SUM_PRIORITIES = SUM_PRIORITIES + get_priority(COMMON_STRING) 

file.close()
print(SUM_PRIORITIES)
