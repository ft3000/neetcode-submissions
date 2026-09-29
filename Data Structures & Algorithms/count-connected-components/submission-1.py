class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        count = 0
        for start in range(n):
            if start in seen:
                continue
            count += 1
            seen.add(start)
            q = deque([start])
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
        return count