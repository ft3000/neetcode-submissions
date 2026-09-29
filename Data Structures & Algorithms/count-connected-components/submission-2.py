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
            q = deque([start])
            while q:
                node = q.popleft()
                seen.add(node)
                for nei in graph[node]:
                    if nei not in seen: 
                        q.append(nei)
        return count