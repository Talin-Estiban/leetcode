#ValidPalindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise. 

Strategy:
- lowercase the input.
- create a verse value which is the input minus chaarcters that are not numbers or letters.
- return true if the reversed version of the created value is equal to the unreversed one. 
"""   
def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        verse=""
        for char in s:
            if char.isalpha() or char in ("0","1","2","3","4","5","6","7","8","9"):
                verse+=char
        return verse[::-1]==verse