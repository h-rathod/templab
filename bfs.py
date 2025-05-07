from collections import deque

def bfs(graph, start):
    # Keep track of visited nodes
    visited = set([start])
    
    # Queue to manage which nodes to visit next
    queue = deque([start])
    
    # Process nodes until queue is empty
    while queue:
        # Get the next node from the front of the queue
        node = queue.popleft()
        print(node)  # Process the current node
        
        # Add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage with the same graph
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

bfs(graph, '5')
