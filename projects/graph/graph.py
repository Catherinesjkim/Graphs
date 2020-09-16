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
        """
        initialize a graph object
        if no dictionary or None is given,
        an empty dictionary will be used
        """
        # empty dictionary and make a set for the values
        # vertices = nodes/lands
        self.vertices = {}
        
    def __repr__(self):
        return str(self.vertices)
    
    def add_vertex(self, vertex_id):
        """
        If the vertex_id "vertex_id" is not in self.__graph_dict, a key "vertex_id" with an empty list as a value is added to the dictionary. Otherwise nothin has to be done
        """
        # Add a vertex/node label to the graph
        if vertex_id not in self.vertices:
            # vertex id = empty set
            self.vertices[vertex_id] = set()

    # Create `add_edge` methods that adds the specified entities to the graph
    # Edge = the connecting line/bridge between two vertices/nodes/lands
    def add_edge(self, v1, v2):
        """
        assumes that edge is a type set, tuple or list;
        between two vertices can be multiple edges!
        """
        # check first if v1 and v2 are in the vertices/nodes
        if v1 in self.vertices and v2 in self.vertices:
            # Add a directed edge/arc to the graph
            # we need to modify our dictionary again
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        A static method generating the edges of the graph "graph". Edges are represented as sets with one (a loop back to the vertex) or two vertices
        """
        # Get all neighbors (edges) of a vertex
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()

    """
    Part 2: Implement Breadth-First Traversal
    Write a function within your Graph class that takes a starting node as an argument, then performs BFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
    """
    def bft(self, starting_vertex):
        # Print each vertex in breadth-first order beginning from starting_vertex.
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    queue.append(neighbor)

    """
    Part 3: Implement Depth-First Traversal with a Stack
    Write a function within your Graph class that takes a starting node as an argument, then performs DFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
    """
    def dft(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex
        visited = set()
        # let S be a stack using double ended queue
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            currNode = stack.pop()
            # if v is not labeled as discovered, then
            if currNode not in visited:
                visited.add(currNode)
                # print its value
                print(currNode)
                # this will return all of the neighbors of the vertices
                for neighbor in self.get_neighbors(currNode):
                    stack.append(neighbor)


    def dft_recursive(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex. This should be done using recursion.
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        # Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order
        pass  # TODO
    
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

    def dfs_recursive(self, starting_vertex, destination_vertex):
        # Return a list containing a path from starting_vertex to destination_vertex in depth-first order. This should be done using recursion
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    # graph.add_vertex(4)
    # graph.add_vertex(5)
    # graph.add_vertex(6)
    # graph.add_vertex(7)
    graph.add_edge('0', '1')
    graph.add_edge('1', '0')
    graph.add_edge('0', '3')
    graph.add_edge('3', '0')
    # graph.add_edge(5, 3)
    # graph.add_edge(6, 3)
    # graph.add_edge(7, 1)
    # graph.add_edge(4, 7)
    # graph.add_edge(1, 2)
    # graph.add_edge(7, 6)
    # graph.add_edge(2, 4)
    # graph.add_edge(3, 5)
    # graph.add_edge(2, 3)
    # graph.add_edge(4, 6)
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
