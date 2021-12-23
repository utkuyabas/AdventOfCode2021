from collections import defaultdict, deque
import sys
import typing


def construct_graph(input) -> dict:
    graph = defaultdict(list)
    for line in input:
        src,dst = line.strip().split("-")
        if dst != "start":
            graph[src].append(dst)
        if src != "start":
            graph[dst].append(src)
    print(graph)
    return graph

def solve(graph : dict) -> int:
    return dfs_inner("start",graph, set(), False)


'''
{'start': ['A', 'b'], 
'A': ['start', 'c', 'b', 'end'], 
'b': ['start', 'A', 'd', 'end'], 
'c': ['A'], 
'd': ['b'], 
'end': ['A', 'b']})


path = start -> A
visited = start
src = A
d_found = false



'''


def dfs_inner(src: str, graph: dict, visited: set, d_found: bool) -> int:
    v = visited.copy()
    if src == "end":
        return 1
    count = 0
    if src in v:
        if not d_found:
            return sum(dfs_inner(dst, graph, v, True) for dst in graph[src] if dst is not "start")
        else:
            return 0

    if src.islower():
        v.add(src)
    return sum(dfs_inner(dst,graph,v, d_found) for dst in graph[src] if dst is not "start")

if __name__ == "__main__":
    all_lines = []
    for line in sys.stdin:
        all_lines.append(line)
    graph = construct_graph(all_lines)
    num_results = solve(graph)
    print(num_results)
