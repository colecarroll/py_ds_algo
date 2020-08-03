'''
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in teh array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers, [2, 4].

O(n) time | O(1) space - where n is the length of the array
'''


def isValidSubsequence(array, sequence):
    seqIndex = 0
    for value in array:
        if seqIndex == len(sequence):
            break
        if sequence[seqIndex] == value:
            seqIndex += 1
    return seqIndex == len(sequence)
