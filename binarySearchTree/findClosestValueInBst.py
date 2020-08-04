# Write a function that takes in a Binary Search Tree(BST) and a target integer value and returns the
# closest valeu to that target value contained in the BST.

# Assume there is only one closest value.

# Each BST has an integer value property called 'value', a 'left' child node, and a 'right' child node. Child nodes can be 'None' or 'null'.

# Recursive solution
# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

def findClosestValueInBstRec(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstRecHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstRecHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstRecHelper(tree.right, target, closest)
    else:
        return closest


# Iterative solution
# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

def findClosestValueInBstIter(tree, target):
    return findClosestValueInBstIterHelper(tree, target, tree.value)


def findClosestValueInBstIterHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
