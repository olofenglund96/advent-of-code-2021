from os import WEXITED
import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from colorama import Fore, Style
import queue
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
import random


def print_grid(grid, index1=None, index2=None):
  dash = "------------"
  printstr = f"{dash}\n"
  for i, row in enumerate(grid.T):
    for j, val in enumerate(row):

      if val:
        add = f"{Fore.BLUE}#{Fore.RESET}"
      else:
        add = f"{Style.DIM}0{Style.RESET_ALL}"

      printstr += add

    printstr += '\n'

  print(printstr, end="")
  print(dash)


def fold_grid(grid, axis, index):
  #print(f"Folding per {axis=}, {index=}")
  ngrid = grid.copy()
  if axis != 0:
    ngrid = ngrid.T

  #print('grid')
 # print_grid(grid)
  #print('ngrid')
  #print_grid(ngrid)
  #print(f"Shape: {ngrid.shape}")

  grid_up, grid_down = ngrid[:index], ngrid[index+1:]

  #print(f"Grid up (shape: {grid_up.shape})")
  #print_grid(grid_up.T)
  #print(f"Grid down (shape: {grid_down.shape})")
  #print_grid(grid_down.T)

  grid_down = grid_down[::-1]
  #print_grid(grid_down.T)

  new_grid = grid_up | grid_down
  #print_grid(new_grid.T)
  if axis != 0:
    return new_grid.T

  return new_grid

@decorators.with_input
def main(lines):
  coords = np.ndarray((len(lines), 2), dtype=np.int32)

  fold_ix = 0
  for i, line in enumerate(lines):
    if line == "":
      fold_ix = i
      break

    f, t = [int(l) for l in line.split(",")]
    coords[i,:] = [f,t]

  coords = coords[:i,:]
  max_x, max_y = np.max(coords[:,0]), np.max(coords[:,1])

  grid = np.zeros((max_x+1, max_y+1), dtype=bool)

  print(grid.shape)

  for cx, cy in coords:
    grid[cx,cy] = 1

  print_grid(grid)

  fold_instructions = []
  for fold_instr in lines[fold_ix+1:]:
    _, _, instr = fold_instr.split(' ')
    instr_axis, instr_ix = instr.split("=")
    fold_instructions.append((instr_axis, int(instr_ix)))

  print(fold_instructions)
  axis_map = {
    'x': 0,
    'y': 1
  }

  for fold in fold_instructions:
    grid = fold_grid(grid, axis_map[fold[0]], fold[1])

    #print(f"grid after folding on {fold}")
    #print_grid(grid)
    #input()

  print_grid(grid)





if __name__ == "__main__":
  main()
