# Isomorphic Strings
"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Strategy:
First solution:
- create a function that counts the occurancies of each letter.
- if the function returns the same result for both strings then they are ismorphic.
Second solution:
- iterate through the strings and create a list containing the index of the letters.the index function returns the index of the first occurance of the letter, by that we build a map that contains where different letters occured multiple times (two of the same index in different places).
"""
# Time limit exceeded
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def numLetters (word):
            result=[]
            for m in range(len(word)):
                count=1
                for n in word[m:]:
                    if m!=len(word)-1:
                        if word[m+1]==n:
                            count+=1
                result.append(count)
            return result
        return (numLetters(s)==numLetters(t))
# Ellevated answer
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def numLetters (word):
            result=[]
            for letter in word:
                result.append(word.index(letter))
            return result
        return (numLetters(s)==numLetters(t))