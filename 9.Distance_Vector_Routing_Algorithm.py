INF = 999

# Read number of nodes
n = int(input("Enter the number of nodes: "))
if n <= 0:
    raise ValueError("Number of nodes must be greater than zero.")

# Read the initial link-cost matrix
print("Enter the cost matrix:")
print("Enter 999 for no direct connection")

cost = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError("Each row must contain exactly n values.")
    if any(value < 0 for value in row):
        raise ValueError("Link costs cannot be negative.")
    cost.append(row)

# Each node initially knows its direct neighbours and itself
dist = [row[:] for row in cost]
for i in range(n):
    dist[i][i] = 0

# Distance Vector updates: exchange routing information until stable
changed = True
while changed:
    changed = False
    previous = [row[:] for row in dist]
    updated = [row[:] for row in previous]

    for i in range(n):
        for destination in range(n):
            for neighbour in range(n):
                if i != neighbour and cost[i][neighbour] < INF:
                    candidate = cost[i][neighbour] + previous[neighbour][destination]
                    if candidate < updated[i][destination]:
                        updated[i][destination] = candidate
                        changed = True

    dist = updated

# Display final distance table
print("\nFinal Distance Table:")
print("    " + "  ".join(f"N{j + 1}" for j in range(n)))

for i in range(n):
    values = ["INF" if value >= INF else str(value) for value in dist[i]]
    print(f"N{i + 1}  " + "  ".join(values))
