
from collections import deque
# Define the Graph
graph = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'A'],
    'C': ['E'],
    'D': ['G'],
    'E': [],   
    'G': []    
}

def bfs(graph, start, goal):
    visited = set()  
    queue = deque([(start, [start])])
    
    while queue:
        current_node, path = queue.popleft()
        print(f"Visiting: {current_node}")

        if current_node == goal:
            print(f"Goal {goal} found!")
            print("Path:", " -> ".join(path))
            return True  

        if current_node not in visited:
            visited.add(current_node)  

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor])) 
    
    print("Goal not found")
    return False 

bfs(graph, 'S', 'G')