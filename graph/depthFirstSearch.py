# You're given a Node class that has a name and an array of optional children nodes.
# When put together, nodes from an acyclic tree-like structure.

# Implement the depthFirstSearch method on the Node class, which takes in an empty array,
# traverses the tree using the Depth-first Search approach (navigating the tree from
# left to right), stores all the of the nodes' names in the input array and returns it.

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(vertices + edges) time | O(v) space
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
