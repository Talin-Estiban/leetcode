#Sort Array by Parity
"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Strategy:
1. my first intuition was iterate through the list and add the values in an even and an odd lists. Then to the result list add the even list and the odd list.
2. in the elevated answer, I created a result list with the same length of the nums list. We iterate through the list and if the number is even we added to the beginning of the list, else (odd number) we add it to the end of the list. 

"""
#first intuition 
 def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for n in nums:
            if n%2==0:
                even.append(n)
            else:
                odd.append(n)
        result=[]
        result.extend(even)
        result.extend(odd)
        return result


#elevated solution:

        result=[1]*len(nums)
        oddCount=len(nums)-1
        evenCount=0
        for n in nums:
            if n%2==0:
                result[evenCount]=n
                evenCount+=1
            else:
                result[oddCount]=n
                oddCount-=1
        return result