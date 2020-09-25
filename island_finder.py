"""
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west. For example:

# 2D Matrix/Array - no diagonal connections - is this an adjacency matrix? Not in an adjacency matrix (rows & columns)

              A  B  C  D  E  F  
islands = A [[0, 1, 0, 1, 0, 0],
          B  [1, 1, 0, 1, 1, 0],
          C  [0, 0, 1, 0, 0, 0], 
          D  [1, 0, 1, 0, 0, 0],
          E  [1, 1, 0, 0, 0, 0]]
          
visited_islands/matrix set
     = [[F, F, F, F, F, F],
        [F, F, F, F, F, F],
        [F, F, F, F, F, F], 
        [F, F, F, F, F, F],
        [F, F, F, F, F, F]]

island_counter(islands) # returns 4

Connected Components = islands: Things representing a land. Social connections - we are trying to find a way to traverse the data when it's a vast data. Similar to word finder problem. We have to be creative and imagine that there is a graph here and see patterns. 

1. Translate the problem into graph terminology

Vertices: 1s
Edges: 1s connected N, S, E, W
Connected Components: Islands

2. Find all islands. Counting how many connected components in this graph? Answer: 4 connected components.

"""

class Stack():
    
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
        
    def size(self):
        return len(self.stack)

# max neighbors = 4 (NSEW) - easier and simpler than word problem
# row index & col index of the current matrix - coordinates: x, y
# 4 if statements, not performance heavy
def get_neighbors(row, col, island_matrix):
    # neighbors array
    neighbors = []
    # check the neighbor above row and col - top
    if row > 0 and island_matrix[row - 1][col] == 1:
        neighbors.append( (row - 1, col) )
    # check the neighbor below row and col - add a row to the value here - bottom
    if row < len(island_matrix) - 1 and island_matrix[row + 1][col] == 1:
        neighbors.append( (row + 1, col) )
        
    # check the neighbor left row and col - now we maniputate the col
    if col > 0 and island_matrix[row][col - 1] == 1:
        neighbors.append( (row, col - 1) )
    
    # check the neighbor right row and col
    if col < len(island_matrix[row]) - 1 and island_matrix[row][col + 1] == 1:
        neighbors.append( (row, col + 1) )

    return neighbors    


# we are going to traverse in this helper function
def dft(starting_row, starting_col, island_matrix, visited):
    # Create an empty stack 
    stack = Stack()
    # push the starting row and col onto Stack
    stack.push((starting_row, starting_col))
    # while stack is not empty:
    while stack.size() > 0:
        # tuple
        # automated mode: dft traversal - it's going to tell us which ones been visited so there are no dupes
        # pop the current row and col off the stack is
        current_row_col = stack.pop()
        row = current_row_col[0]
        col = current_row_col[1]
        # if current row and col NOT visited:
        if visited[row][col] is False:
            # set the current row and col as visited
            visited[row][col] = True
            # get the neighbor rows and col
            for neighbor in get_neighbors(row, col, island_matrix):
                # push them onto the stack
                stack.push(neighbor)
    return visited

    
def island_counter(island_matrix):
    # keep track of lal visited Vertices
    visited_matrix = []
    for i in range(len(island_matrix)):
        visited_matrix.append([False] * len(island_matrix[0]))
    
    island_count = 0
    # walk through each cell of the matrix/array - double for loops, not a graph yet - the loop will tell us to move to the next number. Which way do we want to encode each vertex? Tuple of coordinates (0, 1) - row 0, col 1
    # for each row in the island matrix/array, produce a tuple of coordinates (0, 1) - row 0, col 1
    # row will always the same length 
    for row in range(len(island_matrix)):
        # the length of the inner array = columns
        for col in range(len(island_matrix[row])):
            # if a cell value is 1 and has not been visited, that's the start of a island
            if island_matrix[row][col] == 1 and visited_matrix[row][col] is False: 
                # traverse the connected component (graph) because the islands are connected - vertices and edges - a graph can be a set of graphs
                # what algo to use to traverse? DFT starting at the current cell
                visited_matrix = dft(row, col, island_matrix, visited_matrix)
                # once we are done DFT, that means we have found a new island, a connected component
                # increment some island_count value + 1
                island_count += 1
            
    return island_count   



islands = [[0, 1, 0, 1, 0, 0],
           [1, 1, 0, 1, 1, 0],
           [0, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [1, 1, 0, 0, 0, 0]]

print(island_counter(islands))

# islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# print(island_counter(islands))
