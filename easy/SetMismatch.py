#Set Mismatch
"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Strategy:
- find the duplicate number.
- sum the numbers in the list. calculate Sn which is the sum of the serie.
- calculate the lost number by using this equation: Sn-sumNum+duplicate. such that: Sn-(Sn+duplicate-lost)+duplicate == lost 
"""

def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result=[]
        for n in range(1,len(nums)):
            if nums[n] == nums[n-1]:
                result.append(nums[n])
        sumNum= sum(nums)
        n=len(nums)
        Sn=float(n)/2*(2+(n-1))
        result.append(int((Sn-sumNum)+result[0]))
        return result 