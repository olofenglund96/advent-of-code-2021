import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from colorama import Fore, Style
from pprint import pprint
from collections import defaultdict
import matplotlib.pyplot as plt

point_graph = defaultdict(list)

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

  if min_idx != index and val != 9:
    point_graph[min_idx].append(index)

  if changes == len(indices):
    return -1



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


def get_frame(grid, conns):
  max_i, max_j = 0, 0
  min_i, min_j = grid.shape

  for i, j in conns:
    if i > max_i:
      max_i = i
    if j > max_j:
      max_j = j

    if i < min_i:
      min_i = i
    if j < min_j:
      min_j = j

  return max(min_i-1, 0), max(min_j-1, 0), min(max_i + 2, grid.shape[0]), min(max_j + 2, grid.shape[1])

def print_basin(grid, index, conns):
  i0, j0, it, jt = get_frame(grid, conns)

  dash = "------------"
  printstr = f"{dash}\n"
  printstr += f"size: {len(conns)}\n"
  printstr += f"{dash}\n"
  for i, row in enumerate(grid[i0:it, j0:jt]):
    for j, val in enumerate(row):

      if (i+i0, j+j0) == index:
        add = f"{Fore.RED}{int(val)}{Fore.RESET}"
      elif (i+i0, j+j0) in conns:
        add = f"{Fore.BLUE}{int(val)}{Fore.RESET}"
      else:
        add = f"{Style.DIM}{int(val)}{Style.RESET_ALL}"

      printstr += add

    printstr += '\n'

  print(printstr, end="")
  print(dash)


def bfs_count(grid, points):
  connected = []
  for p in points:
    connected.append(p)
    connected.extend(bfs_count(grid, point_graph[p]))

  return connected



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
      min_points.append(new_idx)
      #print_neighbourhood(grid, (i, j), new_idx, size=5)

      #input()

  basins = dict.fromkeys(min_points, [])

  for idx in min_points:
    connections = [idx]
    connections.extend(bfs_count(grid, point_graph[idx]))
    basins[idx] = connections
    #print_basin(grid, idx, connections)
    # input()


  dash = "------------"
  printstr = f"{dash}\n"
  for i, row in enumerate(grid):
    for j, val in enumerate(row):
      add = f"{Style.DIM}{int(val)}{Style.RESET_ALL}"

      if (i,j) in basins.keys():
        add = f"{Fore.RED}{int(val)}{Fore.RESET}"
      else:
        for basin in basins.values():
          if (i,j) in basin:
            add = f"{Fore.BLUE}{int(val)}{Fore.RESET}"
            break


      printstr += add

    printstr += '\n'

  print(printstr, end="")
  print(dash)


  counts = list(map(lambda b: len(b), basins))

  mul = 1
  for c in sorted(counts)[-3:]:
    mul *= c

  print(mul, sorted(counts)[-5:])

  plt.figure()
  plt.pcolormesh(grid)
  plt.savefig('nice.png')





if __name__ == "__main__":
  main()
