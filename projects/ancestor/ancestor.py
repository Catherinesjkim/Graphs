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
Example Input: 6
Example Output: [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[8,9],[11,8],[10,1]] --> 10

Explanation: Starting at child ID 6, the earliest known ancestor will be parent ID 10, the one at the farthest distance from the input individual. Your ancestry will consist of ID individuals [1,3]->[2,3]->[3,6]->[5,6]->[5,7]->[4,5]->[4,8]->[8,9]->[11,8]->[10,1] --> 10

Plan

1. Translate the problem into graph terminology

Vertex - an ID of parent or child
Edge - link from parent to child
Weights - not needed (no value associated to each link)

2. Build your graph (use adjacency list)

We can build a graph using adjacency list from the input
Key:Value of those keys
Parent:Child Key:Value
Starting individual ID:Earliest ancestor (will be a key in this dict but will have an empty set. No incoming edges)
{
    6: {1, 3}, {2, 3}, {3}, {5}
}

3. Traverse your graph
Will use Depth First Traverse (DFT). Yes, it does matter waht type of traversal will work since we are trying to find the farthest ancestor in an ancestry tree. If we find that the node we're currently on doesn't have any incoming edges, then we've found the farthest ancestor. Need to traverse the entireity of the line. 

Clarifications:
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.

"""
# Function to print ancestors of given node in a binary tree
from collections import deque

# [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9], [11, 8], [10, 1]]
# links = ancestor
def earliest_ancestor(self, ancestors, starting_node):
    if len(ancestors) == 0:
        return ''
    """
    Destination ancestor is Not a value/child in this graph
    graph = {
    6: {1, 3}, {2, 3}, {3}, {5}
    }
    stack = 10
    visited = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9], [11, 8], [10, 1]]
    curr = 10
    """
    graph = self.createGraph(ancestors)
    stack = deque()
    stack.append(ancestors[0][0])
    visited = set()
    while len(stack) > 0:
        # with dfs, we use stack for traversing - stack is on deck like a queue
        starting_node = stack.pop()
        visited.add(starting_node)
        if starting_node not in graph: # curr isnot a value/child (10)
            # because that's the farthest ancestor that will not be a value/child
            return starting_node
        else:
            for neighbor in graph[starting_node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return ''

# return a dict origin/source --> {ancestor}
# ID 10 doesn't have a ancestor, it won't be a value
def createGraph(self, ancestors):
    # empty dictionary
    graph = {}
    # travere all of the edges
    for edge in ancestors:
        parent, child = edge[0], edge[1]
        if parent in graph:
            # parent = key; child = value
            graph[parent].add(child)
        # otherwise
        else:
            # initialize the key
            graph[parent] = { parent }
    return graph
    


