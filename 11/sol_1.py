import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from colorama import Fore, Style
import queue


def print_grid(grid, index1=None, index2=None):
  dash = "------------"
  printstr = f"{dash}\n"
  printstr += f"{dash}\n"
  for i, row in enumerate(grid):
    for j, val in enumerate(row):

      if val > 9:
        add = f"{Fore.BLUE}{9}{Fore.RESET}"
      elif val == -1 or (i, j) == index1:
        add = f"{Fore.RED}{0}{Fore.RESET}"
      elif (i, j) == index2:
        add = f"{Fore.CYAN}{int(val)}{Fore.RESET}"
      else:
        add = f"{Style.DIM}{int(val)}{Style.RESET_ALL}"

      printstr += add

    printstr += '\n'

  print(printstr, end="")
  print(dash)


def get_adjacent_indices(i_max, j_max, i, j, diag=False):
  border = [(i, j-1), (i-1, j), (i+1, j), (i, j+1)]

  if diag:
    border.extend([(i-1, j-1), (i-1, j+1), (i+1, j+1), (i+1, j-1)])

  i_check = []

  for bi, bj in border:
    if bi < 0 or bi >= i_max or \
       bj < 0 or bj >= j_max:
      continue

    i_check.append((bi, bj))

  return i_check


def flash_step(grid):
  flash_indices = np.where(grid > 9)

  for i, j in zip(flash_indices[0], flash_indices[1]):
    adj_indices = get_adjacent_indices(grid.shape[0], grid.shape[1], i, j, diag=True)

    for ai in adj_indices:
      #print_grid(grid, (i,j), ai)
      #input()
      if grid[ai] == -1:
        continue

      grid[ai] += 1

    grid[(i,j)] = -1

  return grid, len(flash_indices[0]) > 0



def step(grid):
  print('step')
  next_grid = grid + 1
  change = True

  while change:
    print_grid(next_grid)
    #input()
    next_grid, change = flash_step(next_grid)
    #print(f"{change=}")

  print_grid(next_grid)
  flashed = np.where(next_grid == -1)
  next_grid[flashed] = 0
  return next_grid, len(flashed[0])



@decorators.with_input
def main(lines):
  grid = np.ndarray((len(lines), len(lines[0])))

  for i, line in enumerate(lines):
    ints = [int(c) for c in list(line)]
    grid[i,:] = ints

  print(grid)

  tot_flashes = 0
  for i in range(100):
    grid, flashes = step(grid)
    tot_flashes += flashes
    #input(f"After step {i+1}")
   # print_grid(grid)

  print(tot_flashes)




if __name__ == "__main__":
  main()
