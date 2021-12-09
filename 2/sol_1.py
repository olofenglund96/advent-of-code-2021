import sys
sys.path.extend(['..', '.'])
import decorators

@decorators.with_cols('./2/input', ('str', 'int'))
def main(lines):
  horz, vert = 0, 0

  for d, v in lines:
    if d == "forward":
      horz += v
    elif d == "down":
      vert += v
    elif d == "up":
      vert -= v

  print(horz * vert)

if __name__ == "__main__":
  main()
