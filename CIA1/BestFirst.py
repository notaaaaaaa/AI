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

# Best First Search (BFS) Algorithm with cost calculation
def best_first_search(start, goal, graph, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start, [start], 0))
    
    visited = set()
    
    while open_list:
        h_value, current_node, path, current_cost = heapq.heappop(open_list)
        
        if current_node == goal:
            return path, current_cost
        
        visited.add(current_node)
        
        for neighbor, edge_cost in graph[current_node].items():
            if neighbor not in visited:
                new_cost = current_cost + edge_cost
                heapq.heappush(open_list, (heuristic[neighbor], neighbor, path + [neighbor], new_cost))
    
    return None, None 

start_node = 'S'
goal_node = 'G'
solution_path, total_cost = best_first_search(start_node, goal_node, graph, heuristic)

print("Best First Search Solution Path:", solution_path)
print("Total Cost:", total_cost)
