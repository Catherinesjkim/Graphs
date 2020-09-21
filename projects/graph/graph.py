"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """
    Represent a graph as a dictionary of vertices mapping labels to edges
    initialize a graph object if no dictionary or None is given, an empty dictionary will be used
    """
    # empty dictionary and make a set for the values
    # vertices = nodes/lands
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph
        If the vertex_id "vertex_id" is not in self.__graph_dict, a key "vertex_id" with an empty list as a value is added to the dictionary. Otherwise nothin has to be done
        """
        # Add a vertex/node label to the graph
        # create new key with vertex id, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    # Create `add_edge` methods that adds the specified entities to the graph
    # Edge = the connecting line/bridge between two vertices/nodes/lands
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        Assumes that edge is a type set, tuple or list; between two vertices can be multiple edges!
        """
        # check first if v1 and v2 are in the vertices/nodes
        # find vertex v1 in our vertices, add v2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        A static method generating the edges of the graph "graph". Edges are represented as sets with one (a loop back to the vertex) or two vertices
        """
        # Get all neighbors (edges) of a vertex
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create empty queue and enque starting vertex
        queue = Queue()
        #
        queue.enqueue(starting_vertex)
        # Create an empty set to track visited vertices
        visited = set()
        # while the queue is not empty
        while queue.size() > 0:
            # get the current vertex(deque)
            node = queue.dequeue()
            # 1
            # check if current vertex has not been visited
            if node not in visited:
                # print current vertex
                # Mark current vertex as visited
                print(node)
                # Add the current vertex to a visited set
                visited.add(node)
                # {1}
            # queue up all the current vertex's neighbors
            # I CANT DO THIS BECAUSE IT RETURN THE NUMBERS, BUT IN A SET AND I CAN'T STORE A SET WITHIN A SET
            # queue.enqueue(self.get_neighbors(node))
                for neighbor in self.get_neighbors(node):
                    queue.enqueue(neighbor)
            # print(queue)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and add the starting vertex
        stack = Stack()
        # create an empty set to track visited vertices
        visited = set()
        stack.push(starting_vertex)
        # while the stack is not empty:
        while stack.size() > 0:
            # get current vertex (destack from stack)
            node = stack.pop()
            # Check if the current vertex has not been visited:
            if node not in visited:
                # print the current vertex/node
                print(node)
                ## mark current vertext as visited
                    # add current vertext to a visited set
                visited.add(node)
                # this will return all of the neighbors of the vertices
                for neighbor in self.get_neighbors(node):
                    stack.push(neighbor)

    # using a python dictionary to act as an adjacency list
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # to keep track of visited nodes
        # Pick any vertex/node, mark it as visited and recur on all its adjacent vertices/nodes.
        visited.add(starting_vertex)
        print(starting_vertex)
        # Repeat until all the nodes are visited, or the node to be searched is found
        # Then for each neighbor of the current node, the dfs function is invoked again
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    # visit all the vertices/nodes of the graph
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create empty queue and enque path to starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # [1]
        # Create an empty set to track visited vertices
        visited = set()
        # while the queue is not empty
        while queue.size() > 0:
            print(queue)
            #  queue = [ [1, 2,3, 5], [1, 2, 4,6] [1,2,4,7]]]
            currrent_path = queue.dequeue()
            # [1, 2, 4]
            print(f'\nthe currrent_path is {currrent_path}')
            current_node = currrent_path[- 1]
            print(f'\nthe current_node is {current_node}')
            # [4]
            if current_node == destination_vertex:
                return currrent_path
            if current_node not in visited:
                visited.add(current_node)
                # {1, 2, 3,4}
                print(f'visted: {visited}')
                for neighbor in self.get_neighbors(current_node):
                    newPath = list(currrent_path)
                    # [1, 2, 4,6]
                    newPath.append(neighbor)
                    # [6]
                    print(f'the new path is: {newPath}')
                    queue.enqueue(newPath)
                    # [[1, 2, 4,6] [1,2,4,7]]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create empty queue and enque path to starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # [1]
        # Create an empty set to track visited vertices
        visited = set()
        # while the queue is not empty
        while stack.size() > 0:
            # get the current vertex path (deque)
            currrent_path = stack.pop()
            # [1, 2]
            print(f'\nthe currrent_path is {currrent_path}')
            # set the current vertex to the last element of the path
            current_node = currrent_path[- 1]
            print(f'\nthe current_node is {current_node}')
            # [2]
            # check if current vertex is destination
            if current_node == destination_vertex:
                return currrent_path
            # check if current vertex has not been visited
            if current_node not in visited:
                # Mark current vertex as visited
                # Add the current vertex to a visited set
                visited.add(current_node)
                # {1, 2}
                print(f'visted: {visited}')
                # queue up new paths with each neighbor
                for neighbor in self.get_neighbors(current_node):
                    newPath = list(currrent_path)
                    # [1,2, 4]
                    newPath.append(neighbor)
                    # [4]
                    print(f'the new path is: {newPath}')
                    # take current path
                    stack.push(newPath)
                    # [1, 2, 3, 4]
                    # append neighbor to it's path
                    # queue up new path
                    
    # base cases - need to know when to return to my base case - when a node is found, you simply return to that node, if not, return to the empty path
    # recursive case - when do you want to recuse the function - find node that you have not yet visited, recurse to that node. 
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """

        # check if you reached the target
        visited.add(starting_vertex)

        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                newPath = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                if newPath is not None:
                    return newPath


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

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
