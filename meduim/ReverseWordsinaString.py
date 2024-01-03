#Reverse Words in a String
"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Strategy:
- use the .split() function which splits the words in the string and gets rid of spaces.
- iterate through the list wich contains the splitted string in a reversed order. Between every word inter a space unless it's the last word.
- in the SECOND intuition in place of adding spaces, we iterate through the list and append the words into a list. Then return the list with spaces between the words using the .join() built in function. 
"""
#First intuition
def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        result=""
        for n in range(len(words)-1,-1,-1):
            result+=words[n]
            if words.index(words[n])!=0: # last word
                result+=" "
        return result

#Second intuition
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        result=[]
        for n in range(len(words)-1,-1,-1):
            result.append(words[n])
        return " ".join(result)