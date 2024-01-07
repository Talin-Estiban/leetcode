#Increasing Triplet Subsequence

"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Strategy:
1. thought of creating lists of length three from the nums list and check if it passses the problem's rules. The triplet numbers can be not subsequent like in this example: [20,100,10,12,5,13]
2. in the second code, we would iterate through the numbers and and always check if the number is larger than the last number we added to the nlist list. If the length of the nlist is 3 that there's an increasing triplet subsequence and we return true.
3. using first_min and second_min variables we keep track of 2 increasing sunsequence numbers and if we have found a third triplet we retuen true. 

"""
1. 66/83 cases passed
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for n in range(len(nums)-2):
            nlist=list(nums[n:n+3])
            if nlist[0]<nlist[1]<nlist[2]:
                return True
        return False

2. 76/83 time limit exceeded
def increasingTriplet(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            nlist=[] #result list for 3 triplet subsequence
            for n in range(len(nums)-2):
                nlist.append(nums[n])
                for i in nums[n:]:
                    if i>nlist[-1]:
                        nlist.append(i)
                        print(nlist)
                        if len(nlist)==3:
                            return True
                    elif i>nlist[0]:
                        nlist.pop()
                        nlist.append(i)
                nlist=[]
            return False

3.Accepted submission
        def increasingTriplet(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            first_min = float('inf')
            second_min = float('inf')
            for num in nums:
                if num <= first_min:
                    first_min = num
                elif num <= second_min:
                    second_min = num
                else:
                    return True

            return False