from os import WEXITED
import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from collections import defaultdict


class Node:
  def __init__(self, data) -> None:
      self.next = None
      self.data = data


class LinkedList:
  def __init__(self, nodes=None) -> None:
    self.head = None

    if nodes is not None:
      self._add_nodes(nodes)

  def _add_nodes(self, nodes):
    node = Node(nodes.pop(0))
    self.head = node
    for n in nodes:
      node.next = Node(n)
      node = node.next

  def __repr__(self) -> str:
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return "".join(nodes)

  def node_count(self):
    counts = defaultdict(int)
    node = self.head

    while node:
      counts[node.data] += 1
      node = node.next

    return counts


def update_template(rules, template):
  node = template.head
  update_list = []
  while node.next:
    pattern = f"{node.data}{node.next.data}"
    update_list.append((node, node.next, rules[pattern]))
    node = node.next

  return update_list


@decorators.with_input
def main(lines):
  template = LinkedList(list(lines[0]))
  rules = {}
  for line in lines[2:]:
    pair, ins = [l.strip() for l in line.split("->")]

    rules[pair] = ins

  for i in range(40):
    print(f"Before iteration {i+1}")
    #print(template)
    #input()
    update_list = update_template(rules, template)

    for n1, n2, poly in update_list:
      node = Node(poly)
      node.next = n2
      n1.next = node


  counts = template.node_count()

  counts_sorted = sorted(counts, key=counts.get)

  min_k, max_k = counts[counts_sorted[0]], counts[counts_sorted[-1]]

  print(max_k - min_k)








if __name__ == "__main__":
  main()
