# Write a function that takes in a non-empty array of distinct integers and an integer representing a # target sum. If any two numbers in the input array sum up to the target sum, the function should
# return them in an array, in any order. If no two numbers sum up to the target sum, the function
# should return an empty array.

# O(n ^ 2) time | O(1) space
def twoNumberSumA(array, targetSum):
    for i in range(len(array - 1)):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# O(n) time | O(1) space


def twoNumberSumB(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# O(nlog(n)) time | O(1) space


def twoNumberSumC(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []