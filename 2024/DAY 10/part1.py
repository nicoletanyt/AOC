from collections import deque

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

MAX_ROW = len(lines)
MAX_COL = len(lines[0])
graph = {} # store graph of pos as neighbours
trailheads = []
total = 0

# identify trailheads and set up graph 
for i in range(MAX_ROW):
    for j in range(MAX_COL):
        adj = []
        for pos in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if pos[0] >= 0 and pos[0] < MAX_ROW and pos[1] >= 0 and pos[1] < MAX_COL:
                # valid adjacent node
                adj.append(pos)
        
        graph[(i, j)] = adj

        if lines[i][j] == "0":
            # trailheads
            trailheads.append((i, j))

def bfs(graph, node, target):
    count = 0
    visited = {}  
    queue = deque() 

    visited[node] = None
    queue.append(node)
    
    while queue:
        pos = queue.popleft() 
        if int(lines[pos[0]][pos[1]]) == target:  
            count += 1
            
        for neighbour in graph[pos]:
            if neighbour not in visited:
                # visit the neighbour only if they have a difference of 1
                if int(lines[pos[0]][pos[1]]) + 1 == int(lines[neighbour[0]][neighbour[1]]):
                    visited[neighbour] = pos  
                    queue.append(neighbour)
    
    return count

for node in trailheads:
    total += bfs(graph, node, 9)

print(total)