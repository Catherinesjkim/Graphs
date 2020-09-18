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

Explanation: Starting at child ID 6, the earliest known ancestor will be parent ID 10, the one at the farthest distance from the input individual. Your ancestry will consist of ID individuals [1,3]->[2,3]->[3,6]->[5,6]->[5,7]->[4,5]->[4,8]->[8,9]->[11,8]->[10,1]] --> 10

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

# A Binary Tree node
class Node:
    
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# If target is present in tree, then prints the ancestors
# and returns true, otherwise returns false
def earliest_ancestor(ancestors, starting_node):
    
    # Base case
    if ancestors == None:
        return False
    
    if ancestors.data == starting_node:
        return True
    
    # If target is present in either left or right subtree,
    # of this node, then print this node
    if (earliest_ancestor(ancestors.left, starting_node) or
        earliest_ancestor(ancestors.right, starting_node)):
        print(ancestors.data)
        return True
    
    # Else return False
    return False

# Driver program to test above function
""" 
```
10
/
1  2   4  11
 \ /  / \ /
  3   5  8
   \ / \   \
    6   7   9
```
Example Input: 6
Example Output: [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9], [11, 8], [10, 1]] --> 10
"""
ancestors = Node(6)
ancestors.left = Node(3)
ancestors.right = Node(5)
ancestors.left.left = Node(1)
ancestors.left.right = Node(2)
ancestors.left.left.left = Node(10)

earliest_ancestor(ancestors, 10)
