# 	Majority Element
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than [n / 2] times. You may assume that the majority element always exists in the array.    

Strategy:
first approach:
- create two lists: one list to save the occuring number and the other list to save number of acuurences.
- iterate through nums and fill the two lists.
- return the number with the most occurencies (ofcaorse it's gonna occur more than n/2).

second approach:
- sort the list nums.
- return the number in the n/2 index of the sorted list. Since this number occures at least n/2 times in the list it's going to occur in the index n/2.
"""
#first approach - counting occurancies 
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=[]
        occur=[]
        for i in range(len(nums)):#iterate through the list
            if nums[i] in num:#if the number is already in num just increase it's occurence.
                x=num.index(nums[i])
                occur[x]+=1
            else:# add the number to num and its accurence is 1. 
                num.append(nums[i])
                occur.append(1)
        return num[occur.index(max(occur))]

# second approach
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=sorted(nums)
        return num[len(num)//2]