#Unique Nmber of Occurences
"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Strategy:
- iterate through the list and create a dictionary, such that it's keys are the value in the list, while it's values are the number of occurence of each value.
- if there's a dublicate in the occurances (values of the dictionary) return true else return false. 
"""
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        occur={}
        for m in arr:
            if m in occur:
                occur[m]+=1
            else:
                occur[m]=1
        values=occur.values() 
        values.sort()
        for m in range(1,len(values)):
            if values[m]==values[m-1]:
                return False
        return True 

        