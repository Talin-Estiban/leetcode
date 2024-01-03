#Two Sum
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Strategy:
- iterate through the list and figure out x which is the other number needed for the sum.
- search for x in the list and if found return the index's.
* the index is used so that not to use the same element twice. 
"""
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=0
        for n in range(len(nums)-1):
            x = target-nums[n] #the other number that completes the sum process
            index+=1
            if x in nums[n+1:]:
                return([n,((nums[n+1:].index(x))+index)])