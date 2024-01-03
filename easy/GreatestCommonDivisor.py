# greatest common divisor of strings- runtime 30ms
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Strategy:
- take the smaller string as a base.
- get the ratio ratio of the lengths of the string (longer one) and the base.
- if the base is concatinated with itself by the "ratio" times and the result is the string then the base is the greatest common divisor.
"""
def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1)>len(str2):// saving the shorter word as the base
            base = str2
            word=str1
        else:
            base = str1
            word = str2
        for i in range(len(base)):
            length = len(word) / len(base) //the ratio between the word and the base
            sample=""
            for j in range(length): // concatenate the base ratio times
                sample += base
            if sample==word: //check if we created the word by concatenating the base
                return(base)
            else:
                base = base[:-1]
        return("")