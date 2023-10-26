# Greatest number of candies

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