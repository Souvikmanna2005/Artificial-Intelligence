# Import heapq for priority queue implementation
import heapq
def astar(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    parent = {} 
    g_cost = {start: 0} 
   
    while open_list: 
        current_f, current_node = heapq.heappop(open_list) 
       
        if current_node == goal: 
            path = [goal] 
       
            while current_node in parent: 
                current_node = parent[current_node] 
                path.append(current_node) 
            return path[::-1] 
       
        for neighbor, cost in graph[current_node]: 
            new_g = g_cost[current_node] + cost 
            if neighbor not in g_cost or new_g < g_cost[neighbor]: 
                g_cost[neighbor] = new_g 
                f_cost = new_g + heuristic[neighbor] 
                parent[neighbor] = current_node 
                heapq.heappush(open_list, (f_cost, neighbor)) 
    return None 
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}
start = 'A' 
goal = 'G' 
path = astar(graph, start, goal, heuristic) 
print("Shortest Path:", path) 