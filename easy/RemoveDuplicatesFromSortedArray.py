# Remove duplicates from sorted array 
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Strategy:
- create index variable  that points to the second element in nums.
- while the index is smaller than the length of nums, examine if the elements in i and i+1 are equal. If yes delete the elment in i.
- else increment i (take the next element's index).
"""
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1#index
        while i<len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
