import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from pprint import pprint



@decorators.with_input
def main(lines):
  fishes = np.array([int(l) for l in lines[0].split(',')])
  #fishes = np.array([2])
  looping_fishes = np.array([0]*7)

  for fish in fishes:
    looping_fishes[fish] += 1

  child_fishes = np.array([0,0])
  day_mod_6 = 0
  for i in range(1, 257):
    num_new_fishes = looping_fishes[day_mod_6]

    looping_fishes[day_mod_6] += child_fishes[0]
    child_fishes[0] = child_fishes[1]

    child_fishes[1] = num_new_fishes
    #print(f"Day {i} mod:({day_mod_6}): {num_new_fishes=}, {looping_fishes=}, {child_fishes=}")
    # fish_list = []
    # for ix, lf in enumerate(looping_fishes):
    #   fish_list.append(((day_mod_6 + ix + 1) % 6, lf))

    #print(f"fishes: {fish_list}")
    #print(f"Tot fishes: {sum(looping_fishes) + sum(child_fishes)}")
    day_mod_6 = i % 7

  print(sum(looping_fishes) + sum(child_fishes))



if __name__ == "__main__":
  main()
