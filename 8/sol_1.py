import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from pprint import pprint


@decorators.with_input
def main(lines):
  count = 0
  for l in lines:
    _, post = l.split("|")
    for word in post.strip().split(" "):
      count += len(word) in (2, 3, 4, 7)


  print(count)








if __name__ == "__main__":
  main()
