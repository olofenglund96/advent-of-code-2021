from functools import reduce
from os import WEXITED
import sys
sys.path.extend(['..', '.'])
import decorators
import heapq as hq
from collections import defaultdict
import numpy as np
from colorama import Fore, Style
import math
from tqdm import tqdm


def parse_list(clist):
  root_list = []
  i = 0
  while i < len(clist):
    i += 1
    if clist[i] == '[':
      sub_list, j = parse_list(clist[i:])
      root_list.append(sub_list)
      i += j + 1

    if clist[i] == ']':
      break

    if clist[i] == ',':
      continue

    root_list.append(int(clist[i]))

  return root_list, i

def add_left(num, i, add):
  while i >= 0:
    if isinstance(num[i], list):
      return add_left(num[i], len(num[i])-1, add)

    if isinstance(num[i], int):
      num[i] += add
      return 0

    i -= 1

  return add

def add_right(num, i, add):
  while i < len(num):
    if isinstance(num[i], list):
      return add_right(num[i], 0, add)

    if isinstance(num[i], int):
      num[i] += add
      return 0

    i += 1

  return add


def explode_number(num, depth):
  i = 0
  while i < len(num):
    subnum = num[i]
    if isinstance(subnum, list):
      if depth == 3: # Explode
        add_left_num, add_right_num = subnum
        print(f"explode {subnum}")
        num[i] = 0
        if add_left_num > 0:
          add_left_num = add_left(num, i-1, add_left_num)
        if add_right_num > 0:
          add_right_num = add_right(num, i+1, add_right_num)

        return add_left_num, add_right_num, True
      else: # Keep going
        add_left_num, add_right_num, action = explode_number(subnum, depth + 1)

      if add_left_num > 0:
        add_left_num = add_left(num, i-1, add_left_num)
      if add_right_num > 0:
        add_right_num = add_right(num, i+1, add_right_num)

      if action:
        return add_left_num, add_right_num, action

    i += 1

  return 0, 0, False


def split_number(num):
  i = 0
  while i < len(num):
    subnum = num[i]
    if isinstance(subnum, int):
      if subnum >= 10:
        print(f"split {subnum}")
        split = subnum / 2
        num[i] = [math.floor(split), math.ceil(split)]
        return True
    else:
      action = split_number(subnum)

      if action:
        return True

    i += 1

  return False


def compute_magnitude(num):
  i = 0
  mags = []
  while i < len(num):
    subnum = num[i]
    if isinstance(subnum, list):
      mags.append(compute_magnitude(subnum))
    else:
      mags.append(subnum)

    i += 1

  return mags[0] * 3 + mags[1] * 2




@decorators.with_input
def main(lines):
  numbers = []
  for line in lines:
    numbers.append(parse_list(line)[0])

  curr_number = numbers.pop(0)

  while len(numbers) > 0:
    next_number = numbers.pop(0)
    #print(curr_number)
    #print(f"+ {next_number}")

    action = True
    comb_num = [curr_number, next_number]
    while action:
      #print(f"{comb_num} ->")
      exploded = True
      did_explode = False

      while exploded:
        _, _, exploded = explode_number(comb_num, 0)

        if exploded:
          did_explode = True


      split = split_number(comb_num)
      #print(f"{comb_num}")
      action = did_explode or split
      #input()

    curr_number = comb_num
    #print(f"= {curr_number}")
    #print()
    #input()

  print(compute_magnitude(curr_number))







if __name__ == "__main__":
  main()
