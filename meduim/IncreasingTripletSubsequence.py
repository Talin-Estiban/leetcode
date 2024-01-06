#Increasing Triplet Subsequence

"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Strategy:
1. thought of creating lists of length three from the nums list and check if it passses the problem's rules. The triplet numbers can be not subsequent like in this example: [20,100,10,12,5,13]

"""
1. 66/83 cases passed
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for n in range(len(nums)-2):
            nlist=list(nums[n:n+3])
            if nlist[0]<nlist[1]<nlist[2]:
                return True
        return False