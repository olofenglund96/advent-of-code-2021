import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from pprint import pprint
from math import copysign


def parse_instructions(lines):
  instr = []
  max_y, max_x = 0, 0
  for l in lines:
    org, _, dest = l.split(" ")
    c_org = tuple([int(c) for c in org.split(",")])
    c_dest = tuple([int(c) for c in dest.split(",")])

    max_x = max(max_x, max(c_org[0], c_dest[0]))
    max_y = max(max_y, max(c_org[1], c_dest[1]))

    instr.append((c_org, c_dest))

  return instr, (max_y+1, max_x+1)

@decorators.with_input
def main(lines):
  instructions, bounds = parse_instructions(lines)

  pprint(instructions)

  grid = np.zeros(bounds)
  print(grid.shape)

  for instr in instructions:
    x0, y0 = instr[0]
    x1, y1 = instr[1]
    if x0 == x1:
      f, t = sorted((y0, y1))
      #print(f, t)
      xind = tuple([x0]*(t-f+1))
      yind = tuple(range(f, t+1))
      indices = (yind, xind)
    elif y0 == y1:
      f, t = sorted((x0, x1))
      #print(f, t)
      yind = tuple([y0]*(t-f+1))
      xind = tuple(range(f, t+1))
      indices = (yind, xind)
    else:
      #fx, tx = sorted((x0, x1))
      #fy, ty = sorted((y0, y1))

      #print(f, t)
      if y1 < y0:
        yind = tuple(range(y0, y1-1, -1))
      else:
        yind = tuple(range(y0, y1+1))

      if x1 < x0:
        xind = tuple(range(x0, x1-1, -1))
      else:
        xind = tuple(range(x0, x1+1))

      indices = (yind, xind)


    print(f"({x0},{y0})->({x1},{y1})")
    print(indices)
    grid[indices] += 1
    print(grid)
    #input()

  print(np.sum(grid > 1))





if __name__ == "__main__":
  main()
