from os import WEXITED
import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from colorama import Fore, Style
import queue
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


def print_paths(paths):
  title = "---- Paths ---"
  print(title)
  for path in paths:
    print_path(path)
  print('-'*len(title))


def ppr(path):
  path_list = []
  for ck, cv in path.items():
    if cv is None:
      path_list.append(['end'])
      continue
    spaths = ppr(cv)
    for sp in spaths:
      #print(sp, ck)
      path_list.append(sp + [ck])

  return path_list


def print_paths_recursive(path_dict):
  path_list = ppr({'start': path_dict})
  print_paths(path_list)


def bfs(graph, root):
  queue = []



def dfs(graph, available_nodes, node, history):
  if node == 'end':
    return None

  history.append(node)
  #print(graph[node])
  ac_nodes = list(filter(lambda n: n.lower() != n or n not in history, graph[node]))
  #print(ac_nodes)

  branches = {}
  for child_node in ac_nodes:
    sub_branches = dfs(graph, available_nodes, child_node, history.copy())
    branches[child_node] = sub_branches

  #for b in branches:
    #print_path(b)

  return branches


@decorators.with_input
def main(lines):
  graph = defaultdict(list)
  for line in lines:
    start, end = line.split('-')
    graph[start].append(end)
    graph[end].append(start)

  #print(graph)

  iters_with_known_paths = 0
  visited_paths = []

  available_nodes = dict.fromkeys(graph.keys(), True)
  print('bfs start')
  paths = dfs(graph, available_nodes, 'start', [])
  print('bfs end')
  #pprint(paths)
  print_paths_recursive(paths)

  path_list = ppr({'start': paths})
  print(len(path_list))



if __name__ == "__main__":
  main()
