"""
Agenda

1. Intro to graphs: A very versatile data structure that allows you to represent relationship between data
    - Social network, flight schedule, word relationships, etc. 

    Components of a Graph:
        - Vertex/node: contains a value - it can contain any arbitrary data. Character, string, or number {}
        
        - Edge/link: connects a pair of nodes - edges can connect nodes in any way possible!
            1. Unidirectional: Path from A to B doesn't mean there's a path from B to A
            2. Bidirectional: A is friends with B, then B is friends with A
            
        - Weight: used to represent a number of value associated with each edge(usually a cost) - each graph/node is an airport(SFO). # of minutes that it takes from SFO to DFW. 

    Examples of Graphs:
        - Social Networks:
            - Each node is a user, edges are friendships between nodes
            - Edges can also be to which groups you are a part of 
            - Transportation Systems (Bart, Maps, etc.)
                - Each node is a location, each edge is a route to another one. A weight can represent time to get there
            - The internet! The link structure of websites can be seen as a graph as well, i.e. a directed graph, because a link is a directed edge or an arc. 
            
        Graphs are oftens used to model problems or situations in physics, biology, psychology and above all in computer science.

        In CS, graphs are used to represent networks of communication, data organization, computational devices, the flow of computation (to represent the data organization, like the file system of an operating system, communication networks).
        

2. Graph Properties:
    - It can have multiple properties: 
    - Know these different properties...
    
    Directed vs. Undirected
        - A graph can be either directed or undirected
        - Directed - An edge from A to B doesn't mean there's an edge from B to A
        - Undirected - An edge from A to B means there's also an edge from B to A
    
    Cyclick vs. Acyclic:
        - Applies to directed graphs
        - Cycle: there's at least one path from a node back to itself
        - Acyclic: there's no paths such that no node can be traversed back to itself
        
    Dense vs. Sparse:
        - A graph can be sparse/dense or anything in between
        - Dense: contains close to the maximum edges possible
        - Sparse: contains close to the minimum edges possible
        
    Weighted vs. Unweighted:
        - A graph can either be weighted or unweighted
        - Weight determines a value associated...

   
3. Representing graphs: Live coding 

    Python has no built-in data type or class for graphs, but it's easy to implement them in Python. One data type is ideal for representing graphs in Python, i.e. dictionaries. 
    
              key : value
    graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
    
    keys = nodes of the graph
    values = lists with the nodes, which are connecting by an edge/link/bridge
    
    An edge/link/bridge can be seen as a 2-tuple with nodes as elements, i.e. ("a", "b")
    
    

    Adjacency List:
        - Use a dictionary with sets to represent the edges of a particular vertex to other neighboring vertices
        - adjacencyList[i] is a list of all the edges to its neighbors for vertex i (Sprint Challenge)
        
    Adjacency Matrix: instead of using dict and sets,
        - Use a matrix to represent whether or not there exists an edge between two vertices 
        - matrix[i][j] is True if there exists an edge from vertex i to vertex j
        
        [[0,1,1,0],
        [0,0,0,1],
        [0,0,0,1],
        [1,0,0,0]]
        
        Rumtime/Space complexities:
            - Space: O(vertices^2) - even in a sparse graph, but good for dense graphs b/c lists are space efficient
            - Add vertex: O(vertices^2)
            - Remove vertex: O(vertices^2)
            - Add edge: O(1) - Constant time
            - Remove edge: O(1)
            - Find edge: O(1)
            - Get all edges: O(vertices)
            
3. Representing graphs: Live coding (0, 1, 2, 3) - a dictionary

0: {1, 2}
1: {3}
2: {3}
3: {0}


Adjacency List Runtime/Space Complexities

Space: O(vertices^2)
    - Imagine a dense graph 
    
Add vertex: O(1)

Remove vertex: O(vertices) - we need to traverse other vertices and remove 

Add edge: O(1) - go to dict constant time and add new value to the set (similar to hash tables)

Remove edge: O(1) - go to dict, find key, remove it from the set

Find edge: O(1) - 5 in the set?

Get all edges: O(1) - 


4. Graph Traversals:

DEPTH-FIRST TRAVERSAL ITERATIVE PSEUDOCODE
    
procedure DFT_iterative(G, vertex) is
    let S be a stack
    S.push(vertex)
    while S is not empty do
        vertex = S.pop()
        if vertex is not labeled as discovered then
            label vertex as discovered
            for all edges from vertex to w in G.adjacentEdges(vertex) do
                S.push(w)
                
                
DEPTH-FIRST TRAVERSAL RECURSIVE PSEUDOCODE
    
procedure DFT_recursive(G, v) is
    label v as discovered
    for all directed edges from v to weight that are in G.adjacentEdges(v) do
        if vertex weight is not labeled as discovered then do
            recursively call DFT_recursive(G, weight)


DFSearch: you stop once you find your goal node


BREADTH-FIRST TRAVERSAL (opposite of DFT)
- Traverse the graph in a breadth-ward motion using a Queue
- Very useful for finding shortest path from node to node


BREADTH-FIRST SEARCH PSEUDOCODE (guided project)

procedure BFS(G, root) is 
    let Q be a queue
    label root as discovered
    Q.enqueue(root)
    while Q is not empty do
        (v := Q.dequeue())
        if v is the goal then
            return v
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as discovered then
                label w as discovered
                w.parent := v
                Q.enqueue(w)


"""
# := assignment expression

# double ended queue: append/pop() left and append/pop() at the end. Stack + queue = deque
from collections import deque

# Adjacency Demo: Similar to Guided Project using adjacencyList
class Graph:

    def __init__(self):
        # empty dictionary and make a set for the values
        self.vertices = {}
        
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            # vertex id = empty set
            self.vertices[vertex_id] = set()
        
    def add_edge(self, v1, v2):
        # check first if v1 and v2 are in the vertices/nodes
        if v1 in self.vertices and v2 in self.vertices:
            # we need to modify our dict again
            self.vertices[v1].add(v2)
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()
    
    
    # Depth First Traversal
    def dft(self, starting_vertex):
        visited = set()
        # let S be a stack using double ended queue
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            currNode = stack.pop()    
            # if v is not labeled as discovered then
            if currNode not in visited:
                visited.add(currNode)
                # print its value
                print(currNode)
                # will return all of the neighbors of the vertices
                for neighbor in self.get_neighbors(currNode):
                    stack.append(neighbor)
                    
    # Breadth First Traversal        
    def bft(self, starting_vertex):
        # so we don't go into circles
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                # we want to make sure that we enqueue the neighbors that we visited
                for neighbor in self.get_neighbors(currNode):
                    queue.append(neighbor)
                    
    
    # Returns path from starting vertex to destination vertex
    def dfs(self, starting_vertex, destination_vertex):
        # use stack and double ended queue
        # stack = [0]
        stack = deque()
        # Each element in the stack is the current path
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
      
                             
g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.dft(0)
print(g)

# Expected output: 
# 0, 2, 3, 1
# 0, 1, 3, 2
    
