# Square root of a number
"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Strategy:
- figure oyt the length of the number x.
- based on the length an according length is connfigured.
- search for the square root of the number in therange and return it.
"""
#First intuition without using any built-in functions. 
def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        y=len(str(x))
        if y==1 or y==2:
            for i in range(0,10):
                if i*i==x or x<(i+1)*(i+1):
                    return(i)
        if y==3 or y==4:
            for i in range(10,100):
                if i*i==x or x<(i+1)*(i+1):
                    return(i)
        if y==5 or y==6:
            for i in range(100,1000):
                if i*i==x or x<(i+1)*(i+1):
                    return(i)
        if y==7 or y==8:
            for i in range(1000,10000):
                if i*i==x or x<(i+1)*(i+1):
                    return(i)
        if y==9 or y==10:
            for i in range(10000,100000):
                if i*i==x or x<(i+1)*(i+1):
                    return(i)
        else:
            for i in range(100000,1000000):
                if i*i==x or x<(i+1)*(i+1):
                    return(i)

# Ellavated answer.
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(floor(sqrt(x)))