import collections

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B','E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}
# BFS algorithm
def bfs(graph, node_start, goal):

    visited, queue = set(), collections.deque([node_start])
    visited.add(node_start)

    while queue:

        # Dequeue a current_node from queue
        current_node = queue.popleft()
        # if goal == current_node:
        #     print('Found it')
        #     break
        print(str(current_node), end=" ")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        #print(visited, queue)
#Driver code
bfs(graph, 'A', 'F')