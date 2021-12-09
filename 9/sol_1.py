import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from colorama import Fore
from pprint import pprint
from collections import defaultdict

memoized_indices = defaultdict(list)

def get_adjacent_indices(i_max, j_max, i, j, diag=False):
  border = [(i, j-1), (i-1, j), (i+1, j), (i, j+1)]

  if diag:
    border.append((i-1, j-1), (i-1, j+1), (i+1, j+1), (i+1, j-1))

  i_check = []

  for bi, bj in border:
    if bi < 0 or bi >= i_max or \
       bj < 0 or bj >= j_max:
      continue

    i_check.append((bi, bj))

  return i_check


def step(grid, index):
  if index in memoized_indices:
    return memoized_indices[index]

  val = grid[index]

  i, j = index

  indices = get_adjacent_indices(grid.shape[0], grid.shape[1], i, j)

  min_val = val
  min_idx = index
  changes = 0
  for ix in indices:
    curr_val = grid[ix]

    if curr_val <= min_val:
      min_val = curr_val
      min_idx = ix
      changes += 1

  if changes == len(indices):
    return -1

  #memoized_indices[min_idx].append(index)
  return min_idx


def print_neighbourhood(grid, index, new_idx, size=1):
  ix, jx = index

  i0, j0 = max(ix - size, 0), max(jx - size, 0)
  it, jt = min(ix+size+1, grid.shape[0]), min(jx+size+1, grid.shape[1])

  dash = "------------"
  printstr = f"{dash}\n"
  for i, row in enumerate(grid[i0:it, j0:jt]):
    for j, val in enumerate(row):

      if (i+i0, j+j0) == index:
        add = f"{Fore.BLUE}{int(val)}{Fore.RESET}"
      elif (i+i0, j+j0) == new_idx:
        add = f"{Fore.RED}{int(val)}{Fore.RESET}"
      else:
        add = str(int(val))

      printstr += add

    printstr += '\n'

  print(printstr, end="")
  print(dash)




@decorators.with_input
def main(lines):
  grid = np.ndarray((len(lines), len(lines[0])))

  for i, line in enumerate(lines):
    ints = [int(c) for c in list(line)]
    grid[i,:] = ints

  min_points = []
  for (i, j), val in np.ndenumerate(grid):
    new_idx = step(grid, (i, j))
    if new_idx == -1:
      continue

    if new_idx == (i, j):
      #print("Low point")
      #print(f"({i}, {j}) = {val} -> {new_idx} = {grid[new_idx]}")
      min_points.append(val + 1)
      #print_neighbourhood(grid, (i, j), new_idx, size=5)

      #input()

  print(len(min_points))
  #print(sum(min_points))




if __name__ == "__main__":
  main()
