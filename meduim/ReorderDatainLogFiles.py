#Reorder Data in Log Files

"""
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
"""

def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit=[]
        letter=[]
        for n in logs:
            if n[-1].isalpha():
                letter.append(n)
            else:
                digit.append(n)
        letter.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        result=letter.extend(digit)
        return letter