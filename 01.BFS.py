from collections import deque
def bfs(graph, start):
    visited = set()  
    queue = deque([start])
    visited.add(start)
    while queue:
        node=queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
bfs(graph, 'A')

'''
OUTPUT
A
B
C
D
E
F
'''