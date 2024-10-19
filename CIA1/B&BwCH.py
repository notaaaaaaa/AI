
import heapq

# Define the graph
graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 0},  
    'E': {},  
    'G': {}   
}

# Define the heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}
# A* Algorithm Function
def a_star(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    
    visited = {}
    
    while queue:
        f_cost, current_cost, current_node, path = heapq.heappop(queue)
        
        if current_node == goal:
            return path, current_cost
        
        if current_node in visited and visited[current_node] <= current_cost:
            continue
        
        visited[current_node] = current_cost
        
        for neighbor, edge_cost in graph[current_node].items():
            total_cost = current_cost + edge_cost 
            f_neighbor_cost = total_cost + heuristic[neighbor] 
            
            heapq.heappush(queue, (f_neighbor_cost, total_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')

start_node = 'S'
goal_node = 'G'

solution_path, solution_cost = a_star(graph, heuristic, start_node, goal_node)

print("A* Algorithm Solution Path:", solution_path)
print("Total Path Cost:", solution_cost)