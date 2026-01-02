#787. Cheapest Flights Within K Stops


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for i,j,p in flights:
            graph[i].append((j,p))
        @cache
        def dfs(s,k):
            if k==-1 and s!=dst:
                return float('inf')
            if s==dst:
                return 0
            ans = float('inf')
            if s not in graph:
                return ans
            for i in graph[s]:
                ans = min(ans,i[1]+dfs(i[0],k-1))
            return ans
        masive = dfs(src,k)
        if masive == float('inf'):
            return -1
        else:
            return masive