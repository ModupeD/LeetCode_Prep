# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Example 1:

# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# Example 2:

# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
 
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # Adjacency list to represent the graph
        adjacency = [[] for _ in range(n)]

        # Populate adjacency list with all the connected nodes
        for edge in edges:
            adjacency[edge[0]].append(edge[1])
            adjacency[edge[1]].append(edge[0])

        # Set to keep track of visited nodes
        visited = set()
        stack = [0]
        visited.add(0)

        # Depth-first search using stack
        while stack:
            node = stack.pop()

            # Iterate over the neighbors of the popped node
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        # If the number of visited nodes equals n, it's a valid tree
        return len(visited) == n
