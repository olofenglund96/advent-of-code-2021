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


def parse_literal(packet, last_packet=False):
  leading_0 = False
  ix = 0
  value = ''
  while not leading_0:
    subp = packet[ix:ix+5]
    leading_0 = subp[0] == '0'
    value += subp[1:]
    ix += 5

  return value, ix


def combine_values(values, type_id):
  type_num = int(type_id, 2)

  if type_num == 0:
    return sum(values)
  if type_num == 1:
    return math.prod(values)
  if type_num == 2:
    return min(values)
  if type_num == 3:
    return max(values)
  if type_num == 5:
    return int(values[0] > values[1])
  if type_num == 6:
    return int(values[0] < values[1])
  if type_num == 7:
    return int(values[0] == values[1])


def parse_subpacket(packet):
  version, type_id = int(packet[:3], 2), packet[3:6]
  values = []
  print(f"{packet=}, {version=}, {type_id=}")
  i = 6

  if type_id == '100':
    literal_value, next_idx = parse_literal(packet[i:])
    i += next_idx
    print(f"literal_value={int(literal_value, 2)}, {next_idx=}")
    return int(literal_value, 2), i
  else:
    lid = packet[i]
    i += 1
    if lid == '0':
      packet_length = int(packet[i:i+15], 2)
      print(f"{packet_length=}")
      i += 15
      j = i
      while j < i + packet_length:
        value, sub_j = parse_subpacket(packet[j:])
        values.append(value)
        j += sub_j
      
      i += packet_length
    else:
      num_packets = int(packet[i:i+11], 2)
      print(f"{num_packets=}")
      i += 11
      for _ in range(num_packets):
        value, j = parse_subpacket(packet[i:])
        i += j
        values.append(value)
      

  return combine_values(values, type_id), i


@decorators.with_input
def main(lines):
  #packet = '9C005AC2F8F0'
  packet = lines[0].strip()
  binary_packet = hex_to_bin(packet)

  version_sum, _ = parse_subpacket(binary_packet)
  print(version_sum)



if __name__ == "__main__":
  main()
