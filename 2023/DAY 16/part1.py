with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

class Node:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
    
    def printNode(self):
        print(str(self.row) + "," + str(self.col) + " direction: " + str(self.direction))
    
    def rtnNode(self):
        return str(self.row) + ", " + str(self.col) + self.direction

max_row = len(lines)
max_col = len(lines[0])
directions = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1)
}
p = {
    "\\" : {
        "N": ["W"],
        "E": ["S"],
        "S": ["E"],
        "W": ["N"],
    },
    "/": {
        "S": ["W"],
        "E": ["N"],
        "W": ["S"],
        "N": ["E"]
    },
    "|": {
        "W": ["N", "S"],
        "E": ["N", "S"],
        "N": ["N"],
        "S": ["S"]
    },
    "-": {
        "N": ["W", "E"],
        "S": ["W", "E"],
        "W": ["W"],
        "E": ["E"]
    }
}

visited = [] # store visited nodes 
queue = [Node(0, 0, "E")] # queue 
energized = set() # answer 

def move(node: Node, visited, energized): 
    if node.row < 0 or node.row == max_row or node.col < 0 or node.col == max_col or node.rtnNode() in visited:
        return None 
    new_nodes = []
    # add location to energized 
    energized.add((node.row, node.col))
    # add node to visited
    visited.append(node.rtnNode())

    # return any continuations in the form of nodes
    if lines[node.row][node.col] in p:
        next_directions = p[lines[node.row][node.col]][node.direction]
        for i in next_directions:
            # make new node with new direction 
            new_node = Node(node.row + directions[i][0], node.col + directions[i][1], i)
            new_nodes.append(new_node)
    else:
        # make new node that continues in same direction
        new_node = Node(node.row + directions[node.direction][0], node.col + directions[node.direction][1], node.direction)
        new_nodes.append(new_node)
    return new_nodes

while queue:
    # new_nodes = expand_node(node in queue)
    new_nodes = move(queue[0], visited, energized)
    # remove the node we just expanded from the queue
    queue.pop(0)

    # add new_nodes to queue
    if new_nodes != None:
        for i in new_nodes:
            if i.row >= 0 and i.row != max_row and i.col >= 0 and i.col != max_col and i.rtnNode() not in visited:
                queue.insert(0, i)
            # print(len(visited))
    
    
print(len(energized))