from collections import defaultdict
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1

        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
    
        for x, y in edges1:
            tree1[x].append(y)
            tree1[y].append(x)
        
        for x, y in edges2:
            tree2[x].append(y)
            tree2[y].append(x)

        def bfs(node, gr, kk):
            if kk == -1:
                return 0
            dist = [inf] * len(gr)
            dist[node] = 0
            ct = 1
            q = deque([node])
            while q:
               cur = q.popleft()
               if dist[cur] == kk:
                   break
               for ch in gr[cur]:
                   if dist[ch] == inf:
                       ct += 1
                       dist[ch] = dist[cur] + 1
                       q.append(ch)
            return ct
        l = [bfs(idx, tree2, k - 1) for idx in range(m)]
        m = max(l)

        return [bfs(idx, tree1, k) + m for idx in range(n)]
        
        
   
        

        

    
            

        

       