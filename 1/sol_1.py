import sys
sys.path.extend(['..', '.'])
import decorators

@decorators.with_ints('./1/input')
def main(lines):
  c = 0
  for i, v in enumerate(lines):
    if i == 0:
      continue

    if lines[i-1] < v:
      c += 1

  print(c)

if __name__ == "__main__":
  main()
