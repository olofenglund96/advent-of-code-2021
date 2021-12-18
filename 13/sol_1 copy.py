from os import WEXITED
import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from colorama import Fore, Style
import heapq as hq
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
import random


def visualise_graph(graph):
  G = nx.Graph()

  for node, connections in graph.items():
    for prio, connection in connections:
     G.add_edge(node, connection, weight=prio)

  plt.figure()
  nx.draw(G, with_labels=True)
  plt.savefig('graph.png')
  plt.close()


def print_node(graph, node):
  connections = graph[node]
  print(f"In {node}, connections: {connections}")

def print_path(path):
  path_rev = path[::-1]
  pstr = ""
  for p in path_rev[:-1]:
    pstr += f"{p},"

  pstr += path_rev[-1]
  print(pstr)


def print_visited_paths(paths):
  title = "---- Visited paths ---"
  print(title)
  for path in paths:
    print_path(path)
  print('-'*len(title))


def dfs(graph, available_nodes, node):
  if node.lower() == node:
    available_nodes[node] = False

  connected_nodes = graph[node]
  ac_nodes = list(filter(lambda n: available_nodes[n[1]], connected_nodes))
  if node == 'end' or len(ac_nodes) == 0:
    return [node]

  #print_node(graph, node)

  lowest_node_val = ac_nodes[0][0]
  matching_nodes = []
  for val, n in ac_nodes:
    if val == lowest_node_val:
      matching_nodes.append((val, n))
      continue

  idx = 0
  if len(matching_nodes) > 1:
    idx = random.randint(0, len(matching_nodes)-1)
  #print(idx)
  next_node = matching_nodes[idx]
  connected_nodes.remove(next_node)

  next_node_count = next_node[0] + 1
  hq.heappush(connected_nodes, (next_node_count, next_node[1]))

  path = dfs(graph, available_nodes, next_node[1])
  return path + [node]


@decorators.with_sample
def main(lines):
  graph = defaultdict(list)
  for line in lines:
    start, end = line.split('-')
    graph[start].append((0, end))
    graph[end].append((0, start))

  #print(graph)

  iters_with_known_paths = 0
  visited_paths = []

  while iters_with_known_paths < 1000:
    available_nodes = dict.fromkeys(graph.keys(), True)
    #print('dfs start')
    path = dfs(graph, available_nodes, 'start')
    #print('dfs end')

    #print_path(path)

    #input()
    if path in visited_paths or path[0] != 'end':
      iters_with_known_paths += 1
      continue

    iters_with_known_paths = 0
    visited_paths.append(path)

    #print_visited_paths(visited_paths)

  vp_str = []
  for vp in visited_paths:
    vp_str.append(",".join(vp[::-1]))

  #for vp
  #print()
  #print_visited_paths(sorted(visited_paths))
  print(len(visited_paths))


if __name__ == "__main__":
  main()
