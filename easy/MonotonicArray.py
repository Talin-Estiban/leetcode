#Monotonic Array

"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Strategy:
- sort the array in a descending and an ascending way. 
- if the array isn't equal to any of them we return False.
"""

    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num1=sorted(nums)
        num2=sorted(nums,reverse=True)
        return (nums==num1 or nums==num2)