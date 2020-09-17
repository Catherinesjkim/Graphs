"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

# Part 1: Graph Class
# Implement a `Graph` class that supports the API in the example below. This means there should be a field `vertices` that contains a dictionary mapping vertex labels to edges.
class Graph:

    # Represent a graph as a dictionary of vertices mapping labels to edges
    def __init__(self):
        """initialize a graph object if no dictionary or None is given, an empty dictionary will be used"""
        # empty dictionary and make a set for the values
        # vertices = nodes/lands
        self.vertices = {}
        
    def __repr__(self):
        return str(self.vertices)
    
    def add_vertex(self, vertex_id):
        """If the vertex_id "vertex_id" is not in self.__graph_dict, a key "vertex_id" with an empty list as a value is added to the dictionary. Otherwise nothin has to be done"""
        # Add a vertex/node label to the graph
        # create new key with vertex id, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            # vertex id = empty set
            self.vertices[vertex_id] = set()

    # Create `add_edge` methods that adds the specified entities to the graph
    # Edge = the connecting line/bridge between two vertices/nodes/lands
    def add_edge(self, v1, v2):
        """Assumes that edge is a type set, tuple or list; between two vertices can be multiple edges!"""
        # check first if v1 and v2 are in the vertices/nodes
        # find vertex v1 in our vertices, add v2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            # Add a directed edge/arc to the graph
            # we need to modify our dictionary again
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        A static method generating the edges of the graph "graph". Edges are represented as sets with one (a loop back to the vertex) or two vertices
        """
        # Get all neighbors (edges) of a vertex
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    """
    Part 2: Implement Breadth-First Traversal
    Write a function within your Graph class that takes a starting node as an argument, then performs BFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
    """
    def bft(self, starting_vertex): 
        # Print each vertex in breadth-first order beginning from starting_vertex.
        # Create an empty queue and enqueue to the starting vertex/node
        queue = deque()
        queue.append(starting_vertex)
        # Create an empty set to track visited vertices
        visited = set()
        
        # while the queue is not empty:
        while len(queue) > 0:
            # get current vertex (deque from queue)
            current_vertex = queue.popleft()
            
            # Check if the current vertex has not been visited:
            # if node not in visited:
            if current_vertex not in visited:
                visited.add(current_vertex)
                # print &  # mark the current vertex
                print(current_vertex)
                for neighbor in self.vertices[current_vertex]:
                    # add current vertex to a visited set
                    # queue up all the current vertex's neighbors (so we can visit them next)
                    queue.append(neighbor)
            

    """
    Part 3: Implement Depth-First Traversal with a Stack
    
    Write a function within your Graph class that takes a starting node as an argument, then performs DFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
    """
    def dft(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex
        
        #Create an empty stack and add the starting vertex
        #create an empty set to track visited vertices

        #while the stack is not empty:
        #get current vertex (destack from stack)

        #Check if the current vertex has not been visited:
        #print the current vertex
            ###mark current vertext as visited
                #add current vertext to a visited set

            #stack up all the current vertex's neighbors (so we can visit them next)
        visited = set()
        # let S be a stack using double ended queue
        stack = deque()
        stack.append(starting_vertex)
        
        while len(stack) > 0:
            current_vertex = stack.pop()
            # if v is not labeled as discovered, then
            if current_vertex not in visited:
                visited.add(current_vertex)
                # print its value
                print(current_vertex)
                # this will return all of the neighbors of the vertices
                for neighbor in self.vertices[current_vertex]:
                    stack.append(neighbor)

    """
    Part 4: Implement Depth-First Traversal using Recursion - Pseudocode
    
    Write a function within your Graph class that takes takes a starting node as an argument, then performs DFT using recursion. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed. 
    
    Algo: 
    1. Pick any vertex/node, mark it as visited and recur on all its adjacent vertices/nodes.
    2. Repeat until all the nodes are visited, or the node to be searched is found
    
    procedure DFT_recursive(G, v) is
        label v as discovered
        for all directed edges from v to weight that are in G.adjacentEdges(v) do
            if vertex weight is not labeled as discovered then do
                recursively call DFT_recursive(G, weight)
                
    Time Complexity
    Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E)O(V+E), where VV is the number of vertices and EE is the number of edges. In case of DFS on a tree, the time complexity is O(V)O(V), where VV is the number of nodes.
    """
    # using a python dictionary to act as an adjacency list
    # dfs_recursive follows the algo described above
    def dft_recursive(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex. This should be done using recursion.
        stack = Stack()  # Stack to keep track of visited nodes
        # Pick any vertex/node, mark it as visited and recur on all its adjacent vertices/nodes.
        # First checks if the current node is unvisited
        stack.push(starting_vertex)
        print("stack is", stack)
        # if yes, it is added in the visited set.
        visited = set()
        # Repeat until all the nodes are visited, or the node to be searched is found
        # Then for each neighbor of the current node, the dfs function is invoked again
        if stack.size() == 0:
            print('here')
            return
            # The base case is invoked when all the nodes are visited. The function then returns
        while stack.size() > 0:
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in self.get_neighbors(node):
                    print(f'The vertices is {node} and the neighbors are {neighbor}')
                    stack.push(neighbor)
        self.dft_recursive(neighbor)
        
       
    """
    Part 5: Implement Breadth-First Search
    
    Write a function within your Graph class that takes a starting node and a destination node as an argument, then performs BFS. Your function should return the shortest path from the start node to the destination node. Note that there are multiple valid paths.

    BFS is an AI search algorithm, that can be used for finding solutions to a problem. 
    
    An effective/elegant method for implementing adjacency lists in Python is using dictionaries. The keys of the dictionary represent nodes, the values have a list of neighbours.
    
    Algo:
    1. Check the starting node and add its neighbours to the queue.
    2. Mark the starting node as explored.
    3. Get the first node from the queue / remove it from the queue
    4. Check if node has already been visited.
    5. If not, go through the neighbours of the node.
    6. Add the neighbour nodes to the queue.
    7. Mark the node as explored.
    8. Loop through steps 3 to 7 until the queue is empty.
    """
    # visit all the vertices/nodes of the graph 
    def bfs(self, starting_vertex, destination_vertex):
        # keep track of all visited nodes
        visited = set()
        # keep track of vertices/nodes to be checked
        queue = [starting_vertex]
        # implement a loop that keeps cycling until queue is empty
        # at each iteration of the loop, a node is checked
        while queue:
            # pop shallowest node (first node) from Queue
            starting_vertex = queue.pop(0)
            if starting_vertex not in visited:
                # if this wasn't visited already, its neighbours are added to queue
                # add node to list of checked nodes
                visited.add(starting_vertex)
                neighbor = self.vertices[starting_vertex]
                
                # add neighbor of node to Queue
                for neighbor in destination_vertex:
                    queue.append(neighbor)
                    
        return visited

    
    """
    Part 6: Implement Depth-First Search
    Write a function within your Graph class that takes takes a starting node and a destination node as an argument, then performs DFS. Your function should return a valid path (not necessarily the shortest) from the start node to the destination node. Note that there are multiple valid paths.
    """
    # Returns path from starting vertex to destination vertex
    def dfs(self, starting_vertex, destination_vertex):
        # Return a list containing a path from starting_vertex to destination_vertex in depth-first order
        # use stack and double ended queue
        # stack = [0]
        stack = deque()
        # Each element in the stack is the current path e.g. [1, 2, 3..]
        # Append the current path that we are on
        stack.append([starting_vertex])
        # visited = 0
        visited = set()
        # keep doing this while the length of the stack is greater than 0
        while len(stack) > 0:
            # currPath = [0] --> [0, 2] --> [0,2,3]
            currPath = stack.pop() # [1, 2, 3]
            # stack = [0, 1],[0,2], [0,2,3] --> go back to the whle loop -->
            # the last node we traversed in the path
            # currNode = 0 --> 2 --> 3
            currNode = currPath[-1] # 3
            if currNode == destination_vertex:
                return currPath
            # if not, add that to the current node
            if currNode not in visited:
                # visited = 0 --> 2 --> 3
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)


    """
    Part 7: Implement Depth-First Search using Recursion
    
    Write a function within your Graph class that takes a starting node and a destination node as an argument, then performs DFS using recursion. Your function should return a valid path (not necessarily the shortest) from the start node to the destination node. Note that there are multiple valid paths.
    
    Depth first search takes a divide and conquer approach, which is implemented using recursion.
    
    Input: A graph G and a vertex v of G
    Output: All vertices reachable from v labeled as discovered   
    
    procedure DFS(G, v) is
    label v as discovered
    for all edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
    
    path = current_path + DFS(sub_tree)
    """
    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        # Return a list containing a path from starting_vertex to destination_vertex in depth-first order. This should be done using recursion
        path.append(starting_vertex)
        
        if starting_vertex == destination_vertex:
            print("find solution path", path)
            starting_vertex = starting_vertex.append(destination_vertex)
            starting_vertex.n += 1
            return
        
        if starting_vertex not in starting_vertex.graph.keys():
            return
        
        neighbors = starting_vertex.graph[starting_vertex]
        for node in neighbors:
            if node not in path:
                # need copy the list otherwise list would persist
                self.dfs_recursive(node, starting_vertex, destination_vertex)

            
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge('0', '1')
    graph.add_edge('1', '0')
    graph.add_edge('0', '3')
    graph.add_edge('3', '0')
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    print(graph.vertices)
    
    """
    Expected output: 
        {'0': {'1', '3'}, '1': {'0'}, '2': set(), '3': {'0'}}
    """

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
