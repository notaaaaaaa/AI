import heapq

# Define the graph 
graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

# Function to find the least-cost path
def find_least_cost_oracle(graph, start, goal):
    queue = [(0, start, [start])] 
    
    min_costs = {node: float('inf') for node in graph}
    min_costs[start] = 0
    
    while queue:
        current_cost, current_node, path = heapq.heappop(queue)
        
        if current_node == goal:
            return path, current_cost
        
        for neighbor, cost in graph[current_node].items():
            total_cost = current_cost + cost
            
            if total_cost < min_costs[neighbor]:
                min_costs[neighbor] = total_cost
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')

start_node = 'S'
goal_node = 'G'

solution_path, solution_cost = find_least_cost_oracle(graph, start_node, goal_node)

print("Least Cost Oracle Path:", solution_path)
print("Total Path Cost:", solution_cost)
