# Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from
# leftmost branch sum to rightmost branch sum.
# A branch sum is the sum of allt he values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that strats at the root node and ends at any leaf node.
# Each Binary Tree node has an integer 'value', a left child node, and a right child node. Children nodes can be either a Binary Tree node themselves of null/None.


# O(n) time | O(n) space - where n is the # of nodes in the Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    branchSumsHelper(root, sums, 0)
    return sums


def branchSumsHelper(tree, sumsList, currentSum):
    newRunningSum = currentSum + tree.value
    if tree.left is None and tree.right is None:
        sumsList.append(newRunningSum)
        return
    if tree.left is not None:
        branchSumsHelper(tree.left, sumsList, newRunningSum)
    if tree.right is not None:
        branchSumsHelper(tree.right, sumsList, newRunningSum)
