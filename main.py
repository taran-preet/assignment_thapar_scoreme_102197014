def longest_path(graph: list) -> int:
    def topological_sort(graph):
        from collections import deque, defaultdict
        
        n = len(graph)
        in_degree = [0] * n
        for u in range(n):
            for v, w in graph[u]:
                in_degree[v] += 1
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor, _ in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return topo_order

    def calculate_longest_path(graph, topo_order):
        n = len(graph)
        dist = [-float('inf')] * n
        
        for node in topo_order:
            if dist[node] == -float('inf'):
                dist[node] = 0
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
        
        return max(dist)

    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

graph = [
       [(1, 10)],
        [(2, 10)],
        [(3, 10)],
        []
]
print(longest_path(graph))  



graph = [
        [(1, 2), (2, 1)],
        [(3, 1)],
        [(3, 5)],
        []
]
print(longest_path(graph))  




graph = [
         [(1, 10)],
        [(2, 10)],
        [(3, 10)],
        []
]
print(longest_path(graph))  


graph = [
         [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
]
print(longest_path(graph))  
print("All test cases pass")

