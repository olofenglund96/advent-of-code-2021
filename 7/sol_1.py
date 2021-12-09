import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from pprint import pprint


@decorators.with_input
def main(lines):
  crabs = np.array([int(l) for l in lines[0].split(',')])
  max_pos = max(crabs)
  min_dist = 1000000
  for i in range(max_pos):
    dist = 0
    for c in crabs:
      dist += abs(i-c)

    min_dist = min(min_dist, dist)

  print(min_dist)





if __name__ == "__main__":
  main()
