import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from pprint import pprint


def step_fish(x):
  y = x - 1
  if y == -1:
    return 6

  return y


@decorators.with_input
def main(lines):
  #fishes = np.array([int(l) for l in lines[0].split(',')])
  fishes = np.array([0])

  for i in range(80):
    num_new_fishes = sum(fishes == 0)
    fishes = np.array([step_fish(f) for f in fishes])

    fishes = np.concatenate((fishes, [8]*num_new_fishes), axis=0)
    print(f"Day {i}: tot fishes:{len(fishes)}, new fishes: {num_new_fishes}. ({fishes})")
    input()


  print(len(fishes))





if __name__ == "__main__":
  main()
