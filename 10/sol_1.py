import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
import queue


@decorators.with_input
def main(lines):
  syms = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }

  scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
  }

  q = []

  tot_score = 0
  for line in lines:
    lc = list(line)
    q.append(lc[0])
    #print(line)
    for i, c in enumerate(lc[1:]):
      if c in syms:
        q.append(c)
        continue

      #print(q)
      last_open = q.pop()
      #print(q, last_open, syms[last_open])
      if syms[last_open] != c:
        tot_score += scores[c]
        #input(f"illegal symbol: {c}, position: {i+1}/{len(lc)}")
        break


  print(tot_score)


if __name__ == "__main__":
  main()
