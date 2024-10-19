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

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()  
    if path is None:
        path = []  
    
    visited.add(start)  
    path.append(start)  
    print(f"Visiting: {start}")

    if start == goal:
        print(f"Goal {goal} found!")
        print("Path:", " -> ".join(path))
        return True 

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited, path):  
                return True  

    path.pop()  
    return False  

dfs(graph, 'S', 'G')