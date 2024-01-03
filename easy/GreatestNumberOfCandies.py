# Greatest number of candies
"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

strategy:
- figure out the maximum number of cadies in the list
- add extracandies to each value in the list and examine if the result is bigger/equal to the max--> add true to the result list, else add false to the result list. 
"""
# first intuition
def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        length = len(candies)
        Lcandy = 0
        result = []
        for i in range(length): // max number of candies in the list
            Lcandy = max(Lcandy,candies[i])
        for i in range(length):
            if (Lcandy <= (candies[i]+extraCandies)): //if the kid has greatest number of candies in the list
                result.append("true")
            else:
                result.append("false")
        return(result)


# second answer / ellavated answer 
def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        length = len(candies)
        Lcandy = max(candies)// max number of candies in the list
        result = []
        for i in range(length):
            result.append(candies[i] + extraCandies >= Lcandy)//if the kid has greatest number of candies in the list
        return(result)