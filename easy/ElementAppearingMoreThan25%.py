# Element Appearing More Than 25% In Sorted Array

"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Strategy:

- My first intiution was to create a dictionary, in which the keys was the values in the given array and the keys were the number of occurance for each one. 
when we have this list we return the number that occured more than 25% of the time in the array. 

- in the elecated answer we calculate quarter index of the array. we iterate through the list and if the value occurs also in the index of the quarter it means that it occurs more than 25%. 

"""

# first intuition 
def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result={}
        for n in arr:
            if n in result.keys():
                result[n]+=1
            else:
                result[n]=1
        for key, value in result.items():
            if value>(len(arr)/4):
                return key

# elevated answer

    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        quart=len(arr)/4
        for i, n in enumerate(arr):
            if arr[i]==arr[i+quart]:
                return arr[i]
