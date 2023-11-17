#Climbing Stairs
"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?   

Strategy:
- initiate the result as 1 since all numbers can be added through summing ones.
- for every set of ones and twos that can be suumed to create n, the probapility of arranging them is: (number of ones+twos)!/ (number of ones)!*(number of twos)!
- if the number can be created through only the sums of twos (y=0) we add this probabilty to the result.
"""
 def climbStairs(self, n):
        import math
        """
        :type n: int
        :rtype: int
        """
        result=1
        flag=True
        index=1# number of twos than can be summed with/out ones to create n 
        while flag:
            y=n-(index*2)#number of ones than can be summed with twos to create n
            if y>0:
                result+=(math.factorial(y+index))/(math.factorial(y)*math.factorial(index))
                index+=1
            elif y==0:
                result+=1
                flag=False
            else:
                flag=False
        return result