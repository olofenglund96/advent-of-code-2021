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



@decorators.with_sample
def main(lines):
  numbers = []
  for line in lines:
    numbers.append(parse_list(line)[0])

  print(numbers)




if __name__ == "__main__":
  main()
