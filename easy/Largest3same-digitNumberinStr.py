#Largest 3 same-digit Number in String
"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:
It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Strategy:
- alternate through the list from the second value to the one before the last. 
- examine if the digit is surrounded by the same-digit numbers.
- add the three numbers by slicing the string, if there was a previous number add the new value just if the new digit is larger.
"""
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result=""
        for n in range(1,len(num)-1):
            if num[n]==num[n-1] and num[n]==num[n+1]:
                if result and num[n]>result[0]:// there is an previous 3 same-digit numbers
                    result=num[n-1:n+2]
                elif not result://the result is empty
                    result=num[n-1:n+2]
        return result 