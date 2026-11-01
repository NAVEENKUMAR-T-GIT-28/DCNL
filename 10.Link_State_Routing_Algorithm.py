INF = 999

# Read number of nodes
n = int(input("Enter the number of nodes: "))
if n <= 0:
    raise ValueError("Number of nodes must be greater than zero.")

# Read cost/adjacency matrix
print("Enter the cost matrix:")
print("Enter 999 for no direct connection")

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError("Each row must contain exactly n values.")
    if any(value < 0 for value in row):
        raise ValueError("Dijkstra's algorithm requires non-negative link costs.")
    graph.append(row)

# Read source node (1-based input)
source = int(input("Enter the source node: ")) - 1
if source < 0 or source >= n:
    raise ValueError("Invalid source node.")

distance = [INF] * n
visited = [False] * n
distance[source] = 0

# Dijkstra's shortest-path algorithm
for _ in range(n):
    min_distance = INF
    current = -1

    for i in range(n):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            current = i

    if current == -1:
        break

    visited[current] = True

    for neighbour in range(n):
        link_cost = graph[current][neighbour]
        if not visited[neighbour] and link_cost < INF:
            new_distance = distance[current] + link_cost
            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance

print("\nShortest Paths from Node", source + 1)
for i in range(n):
    if distance[i] >= INF:
        print(f"Node {source + 1} -> Node {i + 1} : No Path")
    else:
        print(f"Node {source + 1} -> Node {i + 1} : {distance[i]}")
