#Largest Odd Number in String
"""
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Strategy:
- first if the number is odd we return it.
- secondly if number has even numbers at the end we remove them and return it.
- lastly if none of the above we return the biggest odd number in the string. 
"""
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        if int(num)%2!=0:
            return num
        for n in range(len(num)-1,-1,-1):
            if int(num[n])%2==0 :
                num=num[:-1]
            else:
                return num
        else:
            oddNum=[9,7,5,3,1]
            for n in oddNum:
                if str(n) in num:
                    return str(n)
        return ""