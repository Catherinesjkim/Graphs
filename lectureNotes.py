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

DEPTH-FIRST TRAVERSAL ITERATIVE PSEUDOCODE - Use stack and recursion
    
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


BREADTH-FIRST TRAVERSAL (opposite of DFT) - Use queue
- Traverse the graph in a breadth-ward motion using a Queue
- Very useful for finding shortest path from node to node

BREADTH-FIRST SEARCH PSEUDOCODE (guided project) 
- very useful for finding the shortest path from a source to a destination
- Shortest/Nearest path == BFS

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
      
      
    def defs_recursive(self, starting_vertex, destination_vertex):
        # we need a visited set to make sure we keep going back to the visited node
        visited = set()
        return self.dfs_recursive_helper([starting_vertex], destination_vertex, visited)
        
    # Helper method: returns path from starting vertex to destination vertex. Else, returns an empty list
    # It's working as a stack - reason for creating a helper method - you want to pass in the visited set & couldn't find a way to do it in the main fn
    def dfs_recursive_helper(self, curr_path, destination_vertex, visited):
        # what vertex am I on? Last visited curr_vertex in the path
        curr_vertex = curr_path[-1] 
        # base cases - need to know when to return to my base case - when a node is found, you simply return to that node, if not, return to the empty path
        if curr_vertex == destination_vertex:
            # curr_path is where the action is happening
            return curr_path
        
        # mark a node as visited
        visited.add(curr_vertex)
        # otherwise, keep traversing
        for neighbor in self.get_neighbors(curr_vertex):
            if neighbor not in visited:
                # recursive case - when do you want to recuse the function - find node that you have not yet visited, recurse to that node - make a new copy over path - recursion is using a stack implicitly
                newPath = list(curr_path)
                newPath.append(neighbor)
                # what's our curr_path? newPath
                # recursive call: returns the path from the starting vertex to the destination vertex
                # res == result
                res = self.dfs_recursive_helper(newPath, destination_vertex, visited)
                # res is an array
                if len(res) > 0:
                    return res
        
        # return an empty array
        return []
    

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

          
"""
How to solve any graph problem

1. Translate the problem into graph terminology
    - What are the vertices, edges, weights (if needed?)

2. Build your graph
    - Do I even need to build a graph? Should you use an adjacency matrix/list? Yes
    
3. Traverse your graph
    - Should you use BFS/DFS? Do you need an auxiliary data structure?

"""
"""
LeetCode

1. DESTINATION CITY

2. WORLD LADDER: 
    - Find the length of the shortest transformation from beginWord to endWord, each transformation needs to be in wordList
    - Only one letter can be changed at a time
    - Each transformed word must exist in the word list. Note that begin_word is not a transformed word
    
    Note: 
    Return None if there is no such transformation sequence
    All words contain only lowercase alphabetic characters
    You may assume no dupes
    
    Sample: 
    beginWord = "hit",
    endWord = "dog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    ["hit", "hot", "dot", "dog", "cog"]
    
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot", "dog","lot","log"]
    []
    
    
    1. Translate the problem into graph terminology
    
    vertex - a word
    
    edge - a possible one letter transformation from source vertex to another vertex
    hot --d--> dot
    dot --g--> dog
    
    path - series of transformations from one letter source vertex to destination vertex
    
    weights - not needed (no costs associated for each transformation - all equal weights)
    
    
    2. Build your graph - do I need to?
        - we can create all possible transformations of beginWord and all possible transformations of its transformations...BUT that would waste a A LOT OF MEMORY...
        
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]
        ["hit", "hot", "dot", "dog", "cog"]

        stack (vertices to visit) = [["hit", "hot", "dot", "dog", "lot"]]
        dog
        *og
        d*g
        do*
       
    
        - instead, what we can do is to find out the next vertex (word) by coming up with all valid one character transformations and seeing if those are valid vertices to visit (if it's in the word list)
        
    
    3. Traverse the graph

"""
from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
beginWord = "hit",
endWord = "zot",
wordList = [hot","zot"]
["hit", "hot", "zot"]
"""
# find the shortest transformation - bfs
def findLadders(beginWord, endWord, wordList):
    # convert the words into a set/list to perform search more efficiently
    words = set(wordList) # {hot, zot}
    visited = set() # {hit, hot}
    queue = deque() # []
    queue.append([beginWord])
    while len(queue) > 0: # 1
        # currPath is an array
        currPath = queue.popleft() # [hit, hot, zot] - an array of the current transformations
        currWord = currPath[-1] # zot - last element in the array
        if currWord in visited:
            continue # don't do anything, just continue
        visited.add(currWord)
        if currWord == endWord:
            return currPath
        # Determine which vertices to traverse next
        """
        currWord = hot (is it in the wordList?)
        hot
        zot
        h*t
        ho*
        """
        # loop through doc, try out each index of the word
        for i in range(len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i] + letter + currWord[i + 1:]
                # Determine if word is in the word list (if it's a valid vertex to visit)
                if transformedWord in words:
                    # if true, it's a valid transformation and
                    # then we are going to create a new path
                    newPath = list(currPath) # [hit, hot, zot] --> enqueue this
                    newPath.append(transformedWord)
                    queue.append(newPath)
                    
        # if we get to here, we haven't found a valid transformation, then return an empty array
        return []
                    
             
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
                             
    
