graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B','E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs (graph, node_start):
    visited = []
    queue = [node_start]

    while queue:
        current_node = queue.pop(0) #Take neighbor from queue

        if current_node not in visited:
            visited.append(current_node)

            neighbors = graph[current_node]  # get neghbors
            for neighbor in neighbors:
                queue.append(neighbor) #add to queue so that it would come out as current node
            print(current_node, end=" ")

#Driver code
bfs(graph, 'A')
