# Number of 1 Bits

"""
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits
 it has (also known as the Hamming weight).

Strategy:
 - we convert the dicimal number into it's binary form.
 - we add the digits of the binary number and return the result. By adding the digits we learn the number of ones in the binary number. 
"""
def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=bin(n)[2:]
        count=0
        for m in n:
            count+=int(m)
        return count


