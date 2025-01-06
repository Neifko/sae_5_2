import heapq
from typing import List, Dict


class Solution:
    # Implementation for Dijkstra's shortest path algorithm
    def shortestPath(self, n: int, aretes: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []

        # s = src, d = dst, p = poids
        for s, d, p in aretes:
            adj[s].append([d, p])

        # Compute the shortest paths
        shortest = {}
        min_heap = [[0, src]]
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap, [w1 + w2, n2])

        # Fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest

n = 7
edges = [[0,1,3], [0,2,3], [1,3,2], [2,1,4], [2,3,1], [2,4,2], [3,4,5]]
src = 0

solution = Solution()
result = solution.shortestPath(n, edges, src)

print(result)