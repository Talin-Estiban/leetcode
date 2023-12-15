# Contains Duplicate
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Strategy:
- The first intuition was to check item by item n the list and add the to a list (called num). If the item is already in the list num then it occurs twice in the list and we return true.
- The second intuition was to sum all the values in the list. Since the list is made out of sequential ascending numbers, the arithmetic progression series laws can be applied to the list. The sum of this type of series is: (n+1)*n/2 such that n is the last item in the serie. By that we know what the sum of the list should be so if it's not this means there's a dublicate value and we return true.
- Third intuition was to iterate through the list and compare the current index with the value of the index() function, such that if they're not equal this means there's another accurance of this value thus we return True. 
"""
# create list for checked items
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num=[]
        for n in nums:
            if n not in num:
                num.append(n)
            else:
                return True
        return False
        
# Sum of values in the list
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumIndex=sum(nums.index(n) for n in nums)
        return sumIndex!=((len(nums)*(len(nums)-1))/2)

#Index 
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for n in range(len(nums)):
            if nums.index(nums[n])!=n:
                return True
        return False