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


def print_grid(grid):
  dash = "------------"
  printstr = f"{dash}\n"
  printstr += f"{dash}\n"

  for i, row in enumerate(grid):
    for j, val in enumerate(row):

      if val == 1:
        add = "#"
      # elif (i, j) == index2:
      #   add = f"{Fore.CYAN}{int(val)}{Fore.RESET}"
      else:
        add = "."

      printstr += add

    printstr += '\n'

  print(printstr, end="")
  print(dash)


def get_area_indices(i_max, j_max, i, j,):

  top_left_ix = (max(0, i-1), max(0, j-1))
  bottom_right_ix = (min(i_max, i+2), min(j_max, j+2))

  return top_left_ix, bottom_right_ix


def to_bin(area):
  if area.shape != (3, 3):
    print('wrong area')
  bitstr = "".join([str(int(v)) for v in np.hstack(area)])
  return int(bitstr, 2)


def cell_to_num(cell):
  return 1 if cell == '#' else 0


def convolve(grid, algo):
  new_grid = np.zeros(grid.shape)
  for i in range(1, grid.shape[0]-1):
    for j in range(1, grid.shape[1]-1):
      tl_ix, br_ix = get_area_indices(grid.shape[0], grid.shape[1], i, j)
      #print(tl_ix, br_ix)
      val = to_bin(grid[tl_ix[0]:br_ix[0], tl_ix[1]:br_ix[1]])
      new_grid[i,j] = cell_to_num(algo[val])


  return new_grid


@decorators.with_input
def main(lines):
  algo = lines.pop(0)
  lines.pop(0)

  grid = np.zeros((len(lines), len(lines[0])))

  for i, line in enumerate(lines):
    for j, c in enumerate(line):
      if c == '#':
        grid[i,j] = 1

  print_grid(grid)

  grid = np.pad(grid, 1)
  print_grid(grid)
  ng = convolve(grid, algo)
  print_grid(ng)
  ngg = convolve(ng, algo)

  print_grid(ngg)
  print(np.sum(ngg))








if __name__ == "__main__":
  main()
