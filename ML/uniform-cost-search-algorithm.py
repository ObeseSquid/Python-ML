import heapq

# Define the graph with costs
graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('C', 1)],
    'B': [('D', 9), ('C', 3)],
    'C': [('D', 11), ('E', 8)],
    'D': [('C', 11), ('E', 5)],
    'E': [('G', 4)],
    'G': []
}

def ucs(graph, start, goal):
    # Priority queue to store (cost, node, path)
    pq = [(0, start, [])]
    visited = set()  # To keep track of visited nodes

    while pq:
        # Pop the node with the lowest cost
        (cost, node, path) = heapq.heappop(pq)

        # If the node is the goal, return the path and total cost
        if node == goal:
            return path + [node], cost

        if node not in visited:
            visited.add(node)
            path = path + [node]

            # Add neighbors to the priority queue
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + edge_cost, neighbor, path))

    return None, float('inf')  # Return None if no path is found

def main():
    start = 'S'
    goal = 'G'
    path, cost = ucs(graph, start, goal)

    if path:
        print(f"Path found: {path} with total cost: {cost}")
    else:
        print("No path found.")

main()