# Import heapq for priority queue implementation
import heapq #  Import the heapq module which provides an implementation of the queue priority algorithm
def astar(graph, start, goal, heuristic):
    open_list = [] #  Initialize an empty list called open_list This list will likely be used to store nodes or elements that need to be explored
    heapq.heappush(open_list, (heuristic[start], start)) #  Push the starting node to the open priority queue The priority is determined by the heuristic value of the starting node Each element in the heap is a tuple of (heuristic_value, node)
    parent = {} #  Dictionary to store the parent of each node in the path
    g_cost = {start: 0} #  Dictionary to store the cost from the start node to each node
   
    while open_list: #  Main loop continues as long as there are nodes to be explored in the open list
        current_f, current_node = heapq.heappop(open_list) #  Pop the node with the lowest f-score (f = g + h) from the open list         current_f represents the total estimated cost (g + h) of the current path         current_node is the actual node being processed
       
        if current_node == goal: #  Check if the current node is the goal node
            path = [goal] #  If we've reached the goal, create the path with just the goal node
       
            while current_node in parent: #  Traverse from the current node back to the start node using parent pointers
                current_node = parent[current_node] #  Move to the parent node
                path.append(current_node) #  Add the parent node to the path
            return path[::-1] #  Return the reversed path (from goal to start)
       
        for neighbor, cost in graph[current_node]: #  Explore neighbors of the current node
            new_g = g_cost[current_node] + cost #  Calculate the tentative g score for the neighbor
            if neighbor not in g_cost or new_g < g_cost[neighbor]: #  If this path to neighbor is better than any previous one
                g_cost[neighbor] = new_g #  Update the g score
                f_cost = new_g + heuristic[neighbor] #  Calculate the f score (g score + heuristic)
                parent[neighbor] = current_node #  Record the current node as the parent of neighbor
                heapq.heappush(open_list, (f_cost, neighbor)) #  Add neighbor to the open list for further exploration
    return None #  Return None to indicate the absence of a value or to terminate the function
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
start = 'A' #  Define the starting node of the path
goal = 'G' #  Define the goal node that we want to reach
path = astar(graph, start, goal, heuristic) #  Use the A* search algorithm to find the shortest path from start to goal The heuristic parameter guides the search by estimating the cost to reach the goal
print("Shortest Path:", path) #  Print the shortest path found by the A* algorithm