import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np

@decorators.with_strings('./3/input')
def main(lines):
  cidx = 0
  lines_red = lines.copy()
  while cidx < len(lines[0]):
    c = 0
    for l in lines_red:
      c += int(l[cidx])


    filterstr = str(int(c >= len(lines_red) / 2))
    lines_red = list(filter(lambda l: l[cidx] == filterstr, lines_red))
    cidx += 1

  ox = lines_red[0]

  cidx = 0
  lines_red = lines.copy()
  while cidx < len(lines[0]):
    c = 0
    for l in lines_red:
      c += int(l[cidx])


    filterstr = str(abs(int(c < len(lines_red) / 2)))
    lines_red = list(filter(lambda l: l[cidx] == filterstr, lines_red))
    if len(lines_red) == 1:
      break
    cidx += 1

  co = lines_red[0]

  print(int(ox, 2) * int(co, 2))



if __name__ == "__main__":
  main()
