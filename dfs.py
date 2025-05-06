def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)  # Process the current node
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
# Example usage
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

dfs(graph, '5')
