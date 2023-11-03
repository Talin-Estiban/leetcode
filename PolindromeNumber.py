#Polindrome number
"""
Given an integer x, return true if x is a palindrome, and false otherwise.  
Strategy:
- turn x into a list.
- reverse the list and compare it to the original x, if there's a match retuen True 
"""
# first intiution
def polindrome (x):
    num=str(x)
    num_reverse=num[::-1]
    if num==num_reverse:
        return "true"
    else :
        return "false"
# ellavated answer 
def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=list(str(x)) #turning X into a list
        return("".join(y[::-1])==str(x))