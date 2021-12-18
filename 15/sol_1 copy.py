from os import WEXITED
import sys
sys.path.extend(['..', '.'])
import decorators
import heapq as hq
from collections import defaultdict
import numpy as np
from colorama import Fore, Style
import math



def print_grid(grid, queue=None, path=[], explored=[]):
  dash = "------------"
  printstr = f"{dash}\n"
  printstr += f"{dash}\n"
  qpoints = []
  if queue:
    for _, ix in queue:
      qpoints.append(ix)

  for i, row in enumerate(grid):
    for j, val in enumerate(row):

      if (i, j) in path:
        add = f"{Fore.RED}{int(val)}{Fore.RESET}"
      # elif (i, j) == index2:

      #   add = f"{Fore.CYAN}{int(val)}{Fore.RESET}"
      else:
        if explored[(i, j)]:
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


def compute_weight(grid, point):
  dx = abs(point[0] - grid.shape[0])
  dy = abs(point[1] - grid.shape[1])
  dist = dx + dy
  return grid[point] + 0*dist


def compute_path(path_dict, ix):
  path = [ix]
  while ix in path_dict.keys():
    ix = path_dict[ix]
    path.insert(0, ix)

  return path


def bfs(grid, explored, root):
  explored[root] = True
  g_score = {root: 0}
  f_score = {root: compute_weight(grid, root)}

  q = [(root)]
  path_dict = {}
  while len(q) > 0:
    fs = 100000000000
    fn = None
    for i, it in enumerate(q):
      fs_n = f_score[it]
      if fs_n < fs:
        fs = fs_n
        fn = i

    # print(q, f_score)
    # print(q[fn])
    # print(f_score[q[fn]])
    # input()
    i, j = q.pop(fn)
    explored[(i,j)] = False

    if (i, j) == (grid.shape[0] - 1, grid.shape[1] - 1):
      return compute_path(path_dict, (i, j)), explored

    adj_ix = get_adjacent_indices(grid.shape[0], grid.shape[1], i, j)

    for xn in adj_ix:
      new_score = g_score[(i, j)] + grid[xn]
      if xn in g_score and g_score[xn] <= new_score:
        continue

      path_dict[xn] = (i, j)
      g_score[xn] = new_score
      f_score[xn] = new_score + compute_weight(grid, xn)

      if not explored[xn]:
        q.append((xn))
        explored[xn] = True

    # print(f"Queue: {q}")
    # print(f"{path_dict=}")
    # print(f"{g_score=}")
    # print(f"{f_score=}")
    # print_grid(grid, q, compute_path(path_dict, (i, j)))
    # input()



@decorators.with_input
def main(lines):
  grid = np.ndarray((len(lines), len(lines[0])))

  for i, line in enumerate(lines):
    ints = [int(c) for c in list(line)]
    grid[i,:] = ints

  #print_grid(grid)
  explored = np.zeros(grid.shape, dtype=bool)

  path, explored = bfs(grid, explored, (0,0))

  print(explored)

  print_grid(grid, queue=None, path=path, explored=explored)
  tot_sum = 0
  pathstr = ""
  for p in path:
    val = grid[p]
    pathstr += f"{int(val)}->"
    tot_sum += val

  print(pathstr, grid[(0,0)])
  print(tot_sum-grid[(0,0)])
  #print(sum(path))



if __name__ == "__main__":
  main()
