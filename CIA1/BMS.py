# Define the graph
graph = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'A'],
    'C': ['E'],
    'D': ['G'],
    'E': [],
    'G': []
}

def bms(graph, start, goal, path=[]):
    path = path + [start]  
    
    if start == goal:
        return [path]
    
    if start not in graph:
        return []
    
    paths = []
    
    for neighbor in graph[start]:
        if neighbor not in path: 
            new_paths = bms(graph, neighbor, goal, path)
            for new_path in new_paths:
                paths.append(new_path)
    
    return paths

start_node = 'S'
goal_node = 'G'
all_paths = bms(graph, start_node, goal_node)

print("All Possible Paths from", start_node, "to", goal_node, ":")
for path in all_paths:
    print(path)
