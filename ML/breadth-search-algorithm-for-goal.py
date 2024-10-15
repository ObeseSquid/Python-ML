from collections import deque

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D', 'G'],
    'B': ['E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
    
}

def bfs(graph, start, goal):
    visited = set()  # Use set for faster lookups
    queue = deque()  # Use deque for O(1) pops from the front

    visited.add(start)
    queue.append(start)

    while queue:
        s = queue.popleft()
        print(s, end=' ')

        # Check if we have reached the goal
        if s == goal:
            print(f"\nReached goal node: {goal}")
            break  # Stop once the goal is reached

        for n in graph[s]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

def main():
    bfs(graph, 'S', 'G')  # 'G' is the goal node

main()