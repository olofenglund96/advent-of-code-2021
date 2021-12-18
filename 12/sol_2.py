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


def bfs(graph, nvt, root):
  queue = [root]
  nvt[root] -= 1

  while len(queue) > 0:
    node = queue.get()

    for child in graph[node]:
      if child.lower() == child:
        if nvt[child] == 0:
          continue

        nvt[child] -= 1

      queue.append(child)




def dfs(graph, node_tol, node, history):
  if node == 'end':
    return None

  history.append(node)
  #print(graph[node])
  ac_nodes = []
  for n in graph[node]:
    if n.lower() == n:
      hc = 0
      for hn in history:
        if hn == n:
          hc += 1

      if hc >= node_tol[n]:
        continue

    ac_nodes.append(n)

  branches = {}
  for child_node in ac_nodes:
    sub_branches = dfs(graph, node_tol, child_node, history.copy())
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


  small_c = []
  for k in graph.keys():
    if k.lower() == k:
      small_c.append(k)

  node_visit_tol = dict.fromkeys(graph.keys(), -1)
  for sc in small_c:
    node_visit_tol[sc] = 1

  tot_path_list = []
  for sc in small_c:
    if sc in ('start', 'end'):
      continue

    nvt = node_visit_tol.copy()
    nvt[sc] = 2
    #print(f'{sc} can be visited twice')

    #print('bfs start')
    paths = bfs(graph, nvt, 'start')
    #print('bfs end')
    #pprint(paths)
    #print_paths_recursive(paths)
    #input()

    path_list = ppr({'start': paths})
    #print(len(path_list))
    for p in path_list:
      if p not in tot_path_list:
        tot_path_list.extend(p)


  # unique_paths = []
  # for p in tot_path_list:
  #   if p not in unique_paths:
  #     unique_paths.append(p)

  #print_paths(unique_paths)
  print(len(tot_path_list))



if __name__ == "__main__":
  main()
