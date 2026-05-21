
from platform import node
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
def dfs(graph, start, visited,result):
    if start not in visited:
        visited.add(start)
        result.append(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited,result)
visited = set()
traversal_order = []
dfs(graph, 'A', visited,traversal_order)
print(traversal_order)
print("-->".join(traversal_order))


"""
OUTPUT
['A', 'B', 'D', 'E', 'C', 'F']
A-->B-->D-->E-->C-->F
"""