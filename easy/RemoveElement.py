#Remove element
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k. 
   
Strategy:
- create index variable  that points to the first element in nums.
- while the index is smaller than the length of nums, examine if the elements in i is equal to val. If yes delete the elment in i.
- else increment i (take the next element's index).
"""
def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0 #index
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)