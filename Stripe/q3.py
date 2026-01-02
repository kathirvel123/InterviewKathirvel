"""
3. Evaluate division

Problem statement: You are given three arrays:

    equations: A list of pairs, where each equations[i] = [A, B] represents a division equation A / B.
        Each variable A and B is a string representing a unique variable name.
    values: An array of real numbers where values[i] corresponds to the result of the equation equations[i].
        For example, if equations[i] = ["m", "n"] and values[i] = 2.0, this implies m / n = 2.0.
    queries: A list of pairs where each queries[i] = [C, D] asks for the result of the division C / D.

For each query [C, D] in queries, return the result of C / D using the relationships given in equations and values.

    If no valid result can be determined for a query, return -1.0.
"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(values)):
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0],1/values[i]))
        visited = set()
        def dfs(source,dest):
            if source not in graph or dest not in graph:
                return -1
            if source == dest:
                return 1
            if source not in graph:
                return -1
            ans = -1
            for j in graph[source]:
                if j[0] not in visited:
                    visited.add(j[0])
                    ans = max(ans,j[1]*dfs(j[0],dest))
                    visited.remove(j[0])
            return ans
        answer = [0] * len(queries)
        for i in range(len(queries)):
            make = dfs(queries[i][0],queries[i][1])
            if make<0:
                make = -1
            answer[i] = make
        return answer
