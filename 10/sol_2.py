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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
  }

  q = []

  tot_scores = []
  for line in lines:
    lc = list(line)
    q.append(lc[0])
    #print(line)
    ended = True
    for i, c in enumerate(lc[1:]):
      if c in syms:
        q.append(c)
        continue

      #print(q)
      last_open = q.pop()
      #print(q, last_open, syms[last_open])
      #input()
      if syms[last_open] != c:
        #input(f"illegal symbol: {c}, position: {i+1}/{len(lc)}")
        ended = False
        q = []
        break

    if not ended:
      continue

    score = 0
    if len(tot_scores) == -1:
      print(q)
      print(line)
      input()

    while len(q) > 0:
      c = q.pop()
      score *= 5
      score += scores[syms[c]]

    #print(score)
    tot_scores.append(score)

  print(len(tot_scores))
  print(tot_scores)
  print(sorted(tot_scores)[len(tot_scores)//2])


if __name__ == "__main__":
  main()
