#Happy Number
"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Strategy:
First intuition
- it's a direct implementation of the problem's description. But it has a big limitation since I limited the number of iterations to 10!

The elevated answer:
- we iterate while the length of the number is larger than 1, since only the numbers 1 and 7 (one digit numbers) can make a happy number/
"""
# First intuition
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag=0
        while flag<10:
            n=sum(int(num)**2 for num in str(n))
            flag+=1
        if n==1:
            return True
        else:
            return False

#Elevated answer
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while len(str(n))>1:
            n=sum(int(num)**2 for num in str(n))
        if n==1 or n==7:
            return True
        else:
            return False