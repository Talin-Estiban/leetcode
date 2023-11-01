# Can Place Flower 
"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Strategy:
first intiution:
- initiate a parameter x to store the number of flowers we can plant. 
- we iterate through the flowerbed list:
	- on the first value if it's 0--> increment x.
	- in the middle values of the flowerbed if there are 3 corresponding zeros --> increment x.
	- for the last value if it's 0--> increment x.
- compare x and n.

second answer:
- like the first intuition we create a parameter x to store the number of flowers we can plant. 
- iterate through the list:
	- check the right side if it's zero or it's the first value.
	- check the left side if it's zero or it;s the last value.
	- if the two previous conditions are met --> increment x.
- compare x and n.
"""
# first intuition- runtime 33ms 
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        x = 0 # parameter to store num of flowers we can plant
        if n==0: #corner case 
            return(True) 
        for i in range(len(flowerbed)):
            if i==0:
                if len(flowerbed)==1:#corner case
                    return(flowerbed[i]==0)
                elif flowerbed[i]==0 and flowerbed[i+1]==0:
                    x += 1
                    flowerbed[i] = 1
            elif i==(len(flowerbed)-1):
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    x += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    x +=1
                    flowerbed[i] = 1
        return(x >= n)

# ellavated answer but some runtime and memory usage :)
   def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        x = 0 # num of flowers we can plant
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                right_side = (i==0) or (flowerbed[i-1]==0) # check the right side
                left_side = (i==(len(flowerbed)-1)) or (flowerbed[i+1]==0) #check the left side
                if right_side and left_side: #if the value is surrounded by zeros 
                    flowerbed[i] = 1
                    x +=1
        return (x>=n)