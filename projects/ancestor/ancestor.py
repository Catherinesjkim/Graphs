"""
Similar to destination city problem
Key:Value
Parent:Child (patent)
Source vertex: find the earliest ancestor (priority!)

Understand

```
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
```
Example Input: [(1, 3), (2, 3), (3, 6)]
Starting node: 6
output: 1 (1 and 2 are tied but 1 has a lower id)

starting node: 1
output: -1 (1 has no ancestor)

Explanation: Starting at child ID 6, the earliest known ancestor will be parent ID 10, the one at the farthest distance from the input individual. Your ancestry will consist of ID individuals [1,3]->[2,3]->[3,6]->[5,6]->[5,7]->[4,5]->[4,8]->[8,9]->[11,8]->[10,1] --> 10


Plan
1. Translate the problem into graph terminology
Vertex - a person (in this case, we're given their IDs)
Edge - parent-child relationship between two people
Weights - not needed, all edges are equal and have no value/cost relted to them

2. Build your graph (use adjacency list)
Build a graph by using the parent-child relationships/edges we're givein (adjacency list from the input). Each node in the graph will have an outgoing/directed edge to tis parent/ancestor.

Key:Value of those keys
Parent:Child Key:Value

Starting individual ID:Earliest ancestor (will be a key in this dict but will have an empty set. No incoming edges)
{
    6: {1, 3}, {2, 3}, {3}, {5}
}

3. Traverse your graph
We traverse the graph while keeping track of the node's distances from the starting and keep track of the terminal node with the lowest id and greatest distance. A terminal will have no outgiong edges, meaning it has no more ancestors. A terminal node doesn't mean it's the earliest ancestor though, so we need to consider the terminal node that is the greatest distance from the starting node (that also has the lowest id).

In this case, we can use Depth-First Traverse (DFT) to traverse all of the starting node's ancestors and return the earliest one with the lowest ID. Yes, it does matter waht type of traversal will work since we are trying to find the farthest ancestor in an ancestry tree. If we find that the node we're currently on doesn't have any incoming edges, then we've found the farthest ancestor. Need to traverse the entireity of the line. 

Clarifications:
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.

 Destination ancestor is Not a value/child in this graph
    graph = {
    6: {1, 3}, {2, 3}, {3}, {5}
    }
    stack = 10
    visited = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9], [11, 8], [10, 1]]
    curr = 10

"""

from collections import deque

def earliest_ancestor(ancestors, starting_node):
    # A tuple with a node and its distance from the starting node
    # At the beginning, the starting node's earliest ancestor is itself
    stack = deque()
    graph, paths = createGraph(ancestors), []
    stack.append([starting_node])

    while len(stack) > 0:
        # with dfs, we use stack for traversing - stack is on deck like a queue
        current_path = stack.pop()
        current_vertex = current_path[-1]

        # This checks if the node is a terminal node
        if current_vertex in graph: # curr is not a value/child (10)
            # Only consider terminal nodes that have a greater distance than the ones we've found so far
            for neighbor in graph[current_vertex]:
                # because that's the farthest ancestor that will not be a value/child
                new_path = list(current_path)
                new_path.append(neighbor)
                stack.append(new_path)
                
        # If there's a tie then choose the ancestor with the lower id
        elif current_vertex != starting_node:
            if not len(paths):
                paths.append(current_path)
            elif len(current_path) > len(paths[0] or current_path[-1] < paths[0][-1]):
                paths = [current_path]
                
    # If the starting node's earliest ancestor is itself, then just return -1
    return paths[0][-1] if len(paths) else -1

# Creates a graph where the keys are a node and its values are its ancestors
# return a dict origin/source --> {ancestor}
# ID 10 doesn't have a ancestor, it won't be a value
def createGraph(ancestors):
    # This convenience method simply allows us to initialize default values when assigniing
    # a key to a dictionary. In this case, the default value for a new key is an empty set
    # empty dict
    graph = {}
    # travere all of the edges
    for pair in ancestors:
        edge, vertex = pair[0], pair[1]
        if vertex not in graph:
            # parent = key; child = value
            graph[vertex] = set()
        # initialize the key - add edge to the key in the graph
        graph[vertex].add(edge)
    # otherwise
    return graph
    


