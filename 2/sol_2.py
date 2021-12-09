import sys
sys.path.extend(['..', '.'])
import decorators

@decorators.with_cols('./2/input', ('str', 'int'))
def main(lines):
  horz, vert, aim = 0, 0, 0

  for d, v in lines:
    if d == "forward":
      vert += v*aim
      horz += v
    elif d == "down":
      aim += v
    elif d == "up":
      aim -= v

  print(horz * vert)

if __name__ == "__main__":
  main()
