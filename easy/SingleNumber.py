#Single Number
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Strategy:
- we iterate through the list '(len(nums)+1)/2' times such that  this is the number of not equal numbers. Since there are len(nums)-1 equal couple numbers.
- with every iteration we save the first number and delete. then we search for that number in the list, if it's none existent then we return (it's a single number). Else we remove the second appearance of the number and move on to the second value.
"""
   def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in range((len(nums)+1)/2):
            number=nums[0]
            nums.pop(0)
            if number in nums:
                nums.pop(nums.index(number))
            else:
                return number
        

 

