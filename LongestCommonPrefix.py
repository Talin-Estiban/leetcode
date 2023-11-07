#Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Strategy:
- we start with the first letter of the first word and if all worlds have it common, we take the first two letters and so on...
- if there wasn't a match we remove the last letter we added since it;s not in common.
- if there's no letters in common we retuen"".
"""
 def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=""
        index=0
        for n in strs[0]:#iterate through the letters of the first string
            result+=n
            index+=1
            for i in range(len(strs)): #check for common prefix in the rest strings
                word=strs[i]
                if result !=word[0:index]:
                    result=result[:(len(result)-1)]
                    return result 
        return result