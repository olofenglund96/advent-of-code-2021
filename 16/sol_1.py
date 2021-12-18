from os import WEXITED
import sys
sys.path.extend(['..', '.'])
import decorators
import heapq as hq
from collections import defaultdict
import numpy as np
from colorama import Fore, Style
import math


def hex_to_bin(hex):
  htb_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
  }

  bitstr = ""
  for c in hex:
    bitstr += htb_map[c]

  return bitstr


def parse_literal(packet):
  leading_0 = packet[0] == '0'
  ix = 0
  while not leading_0:
    subp = packet[ix+1:ix+5]
    leading_0 = subp[0]
    ix += 5






def parse_subpacket(packet):
  binary_packet = hex_to_bin(packet)
  version, type_id = binary_packet[:3], binary_packet[3:6]

  if type_id == '100':
    next_idx = parse_literal(binary_packet[7:])

  print(version, type_id)


@decorators.with_sample
def main(lines):
  sub_packet = 'D2FE28'

  parse_subpacket(sub_packet)



if __name__ == "__main__":
  main()
