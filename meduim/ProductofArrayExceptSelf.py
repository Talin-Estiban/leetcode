#Product of Array Except Self

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Strategy:
- we know thatin multiplication, if we multiply the number by one thw result is the number itself. So I've used this property such that in every iteration the number is turned into one (it won't affect the product result). So in every iteration the number is turned into one, all the numbers are multiplied and the result is appended in the result list.
"""
# First intuition-Time limit exceded 18/22 testcases passed
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)):
            nlist=list(nums)
            nlist[i]=1
            mult=1
            for n in nlist:
                mult*=n
            result.append(mult)
        return result

# Right solution
def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products

