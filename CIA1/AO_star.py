import math

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

# AO* algorithm function
def ao_star(node, graph, heuristic, goal, visited):
    if node == goal:
        return 0, [goal]
    
    if node in visited:
        return math.inf, []
    
    visited.add(node)
    
    min_cost = math.inf
    best_subtree_path = []

    for child_node, cost in graph[node].items():
        subtree_cost, subtree_path = ao_star(child_node, graph, heuristic, goal, visited)
        total_cost = cost + subtree_cost

        if total_cost < min_cost:
            min_cost = total_cost
            best_subtree_path = [node] + subtree_path
    
    visited.remove(node) 

    return min_cost, best_subtree_path

def run_ao_star(start_node, goal_node):
    visited = set()
    total_cost, solution_path = ao_star(start_node, graph, heuristic, goal_node, visited)
    return solution_path, total_cost

start_node = 'S'
goal_node = 'G'
solution_path, total_cost = run_ao_star(start_node, goal_node)

print("AO* Solution Path:", solution_path)
print("Total Cost to Goal:", total_cost)
