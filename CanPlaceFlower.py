# Can Place Flower 

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