import random

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

# Heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

def greedy_solution(graph, heuristic, start, goal):
    current_node = start
    solution = [current_node]
    
    while current_node != goal:
        neighbors = graph[current_node]
        if not neighbors:
            break
        next_node = min(neighbors, key=lambda n: heuristic[n])
        if next_node not in solution:  # Avoid cycles
            solution.append(next_node)
        current_node = next_node
    
    return solution

def path_cost(heuristic, solution):
    return sum([heuristic[node] for node in solution])

def generate_neighbors(solution):
    neighbors = []
    for i in range(1, len(solution) - 1):  # Exclude the start and goal nodes from swapping
        for j in range(i + 1, len(solution) - 1):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Swap nodes
            neighbors.append(neighbor)
    return neighbors

def best_neighbor(graph, heuristic, current_solution):
    neighbors = generate_neighbors(current_solution)
    
    best_neighbor = current_solution
    best_cost = path_cost(heuristic, current_solution)
    
    for neighbor in neighbors:
        current_cost = path_cost(heuristic, neighbor)
        if current_cost < best_cost:
            best_cost = current_cost
            best_neighbor = neighbor
    
    return best_neighbor, best_cost

# Hill Climbing Algorithm
def hill_climbing(graph, heuristic, start, goal):
    current_solution = greedy_solution(graph, heuristic, start, goal)
    current_cost = path_cost(heuristic, current_solution)
    
    while True:
        neighbor, neighbor_cost = best_neighbor(graph, heuristic, current_solution)
        
        if neighbor_cost >= current_cost:
            print(f"Reached local optimum at {current_solution} with cost {current_cost}")
            break
        
        current_solution = neighbor
        current_cost = neighbor_cost
    
    return current_solution, current_cost

start = 'S'
goal = 'G'
solution, cost = hill_climbing(graph, heuristic, start, goal)

print("Final Solution Path:", solution)
print("Final Path Cost:", cost)
