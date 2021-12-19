from os import WEXITED
import sys

from numpy.lib.arraysetops import unique
sys.path.extend(['..', '.'])
import decorators
import heapq as hq
from collections import defaultdict
import numpy as np
from colorama import Fore, Style
import math
from tqdm import tqdm


def in_target(target, point):
  in_x = point[0] >= target[0][0] and point[0] <= target[0][1]
  in_y = point[1] >= target[1][0] and point[1] <= target[1][1]

  return in_x and in_y

def throw_probe(velocity, midpoint, target):
  pos = np.array([0, 0])
  #print(f"{midpoint=}")
  while True:
    if in_target(target, pos):
      #print(f"In target, {pos=}")
      return True

    #print(f"{pos=}")
    if pos[0] > target[0][1] or pos[1] < target[1][0]:
      #print("Overshot")
      return False

    pos += velocity

    if velocity[0] > 0:
      velocity[0] -= 1
    elif velocity[0] < 0:
      velocity[0] += 1

    velocity[1] -= 1



@decorators.with_input
def main(lines):
  line = lines[0]
  start, end = line.find('='), line.find(',')
  x1, x2 = [int(i) for i in line[start+1:end].split("..")]

  line = line[end:]
  start, end = line.find('='), len(line)
  y1, y2 = [int(i) for i in line[start+1:end].split("..")]
  target = [(x1, x2), (y1, y2)]
  midpoint = np.array([x1 + abs(x1 - x2)//2, y1 + abs(y1 - y2)//2])
  print(f"Target Y size: {y2-y1}")
  vels_in_target = []
  for j in tqdm(range(-200, 200)):
    for i in range(200):
      velocity = np.array([i, j])
      #print(f"Velocity {velocity}, throwing..")
      in_t = throw_probe(velocity, midpoint, target)
      if in_t:

        vels_in_target.append((velocity[0], velocity[1]))

  unique_vels = set(vels_in_target)
  print(unique_vels)
  print(len(vels_in_target), len(unique_vels))





if __name__ == "__main__":
  main()
