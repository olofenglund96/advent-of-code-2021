import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from pprint import pprint


def get_number(positions, word):
  if len(word) == 2:
    return 1
  elif len(word) == 3:
    return 7
  elif len(word) == 4:
    return 4
  elif len(word) == 7:
    return 8

  pos =  {
    0: ['t', 'tl', 'tr', 'bl', 'b', 'br'],
    2: ['t', 'tr', 'm', 'bl', 'b'],
    3: ['t', 'tr', 'm', 'br', 'b'],
    5: ['t', 'tl', 'm', 'br', 'b'],
    6: ['t', 'tl', 'm', 'bl', 'br', 'b'],
    9: ['t', 'tl', 'tr', 'br', 'b', 'm']
  }


  for k, v in pos.items():
    word_from_pos = "".join([positions[c] for c in v])
    if len(word) == len(word_from_pos) and \
       all(w in word_from_pos for w in word):
       return k


@decorators.with_input
def main(lines):
  codes = []

  for l in lines:
    i, o = l.split('|')
    codes.append((i.strip().split(" "), o.strip().split(" ")))

  #codes = [("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" "),
   #         "cdfeb fcadb cdfeb cdbaf".split(" "))]

  tot_sum = 0
  for start, end in codes:
    numbers = [None]*10
    positions = {
      't': None,
      'tl': None,
      'tr': None,
      'm': None,
      'bl': None,
      'br': None,
      'b': None
    }

    del_idx = []
    for i, word in enumerate(start):
      if len(word) == 2:
        numbers[1] = word
        del_idx.append(i)
      elif len(word) == 3:
        numbers[7] = word
        del_idx.append(i)
      elif len(word) == 4:
        numbers[4] = word
        del_idx.append(i)
      elif len(word) == 7:
        numbers[8] = word
        del_idx.append(i)

    for ix in sorted(del_idx, reverse=True):
      del start[ix]

    #print(start, numbers[7])

    positions['t'] = list(set(numbers[7]) - set(numbers[1]))[0]

    tr_br = list(set(numbers[7]) - set(positions['t']))
    d = dict.fromkeys(tr_br, 0)
    for word in start:
      intersect = set(word).intersection(set(numbers[7]))
      if len(intersect) == 2:
        d[list(set(intersect) - set(positions['t']))[0]] += 1

    for k, v in d.items():
      if v == 1:
        positions['tr'] = k
      elif v == 2:
        positions['br'] = k

    del_idx = -1

    for i, word in enumerate(start):
      if len(word) == 5 and len(set(word).intersection(set(numbers[7]))) == 3:
        numbers[3] = word
        del_idx = i
        break

    del start[del_idx]

    inte = set(numbers[4]).intersection(set(numbers[3]))

    for c in inte:
      if c not in positions.values():
        positions['m'] = c

    del_idx = -1
    for i, word in enumerate(start):
      inte = set(numbers[8]).intersection(word)
      if len(inte) == len(numbers[8]) - 1 and positions['m'] not in word:
        numbers[0] = word
        del_idx = i
       # print(word)

    del start[del_idx]

    for c in numbers[4]:
      if c not in positions.values():
        positions['tl'] = c

    for c in numbers[3]:
      if c not in positions.values():
        positions['b'] = c

    for c in numbers[0]:
      if c not in positions.values():
        positions['bl'] = c


    pprint(positions)
    #print(start)
    numbers = []
    for word in end:
      numbers.append(str(get_number(positions, word)))

    #print(numbers)
    tot_sum += int("".join(numbers))


  print(tot_sum)










if __name__ == "__main__":
  main()
