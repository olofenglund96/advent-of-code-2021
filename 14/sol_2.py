from os import WEXITED
import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from collections import defaultdict


def update_template(rules, template):
  new_template = ""
  i = 0
  for i in range(len(template)-1):
    pattern = template[i:i+2]
    #print(pattern)
    new_template += f"{pattern[0]}{rules[pattern]}"
    #print(new_template)
    #input()

  return f"{new_template}{template[-1]}"

def print_combined_patterns(patterns):
  pstr = ""
  for val in patterns.values():
    pstr += val[:-1]

  pstr += val[-1]
  print(pstr)

@decorators.with_input
def main(lines):
  template = lines[0]
  rules = {}
  counts = defaultdict(int)
  for line in lines[2:]:
    pair, ins = [l.strip() for l in line.split("->")]

    rules[pair] = ins

  for i in range(len(template)-1):
    counts[template[i:i+2]] += 1

  #print(counts)
  for i in range(40):
    next_counts = defaultdict(int)

    for k, v in counts.items():
      if k in rules:
        ins = rules[k]
        p1 = k[0] + ins
        p2 = ins + k[1]
        next_counts[p1] += v
        next_counts[p2] += v
      else:
        next_counts[k] += v

    counts = next_counts
    #print(counts)
   # input()

  char_counts = defaultdict(int)

  for k, v in counts.items():
    char_counts[k[0]] += v

  char_counts[template[-1]] += 1
  #print(char_counts)
  sorted_counts = sorted(char_counts, key=char_counts.get)
  #print(sorted_counts)
  print(char_counts[sorted_counts[-1]] - char_counts[sorted_counts[0]])


if __name__ == "__main__":
  main()
