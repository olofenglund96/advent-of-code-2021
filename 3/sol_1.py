import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np

@decorators.with_strings('./3/input')
def main(lines):
  print(lines[:5])
  bit_counts = np.array([0]*len(lines[0]))
  for l in lines:
    bit_counts += np.array([int(ls) for ls in list(l)])

  most_common_bits = np.round(bit_counts / len(lines))
  bitstr = "".join(most_common_bits.astype(int).astype(str))
  mcb = int(bitstr, 2)
  print(mcb, bitstr)

  least_common_bits = np.abs(most_common_bits - 1)
  bitstr = "".join(least_common_bits.astype(int).astype(str))
  lcb = int(bitstr, 2)

  print(mcb * lcb)



if __name__ == "__main__":
  main()
