# merge strings alternately
"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Strategy:
first intuition:
- find the difference between the two lengths of the strings.
 	- if it's zero then the two words have the same lngth then just merge them based on the length.
	- else one of the two strings is longer and after merging based on the shorter string add what's left from the larger one. 

second approach:
- figure out which word is longe--> our index.
- merge the two strings by using the index, while the iteration count is smaller than the index merge the next letter of the word if the iteration is smaller than it's length.
"""

 # my first intuition- 30ms runtime
def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word=""
	// check if one word is longer that the other
        length = len(word1)-len(word2)
        if length==0:
	    // add letters from both words alternatvely
            for i in range(len(word1)):
                word += (word1[i]+word2[i])
        else:
            if length>0:
                for i in range(len(word2)):
                    word += (word1[i]+word2[i])
                word += word1[length:] //word1 is longer--> add the rest to the end
            else:
                for i in range(len(word1)):
                    word += (word1[i]+word2[i])
                word += word2[length:]//word2 is longer--> add the rest to the end
        return(word)

#second approach- 19ms runtime
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word = ""
        index = max(len(word1),len(word2)) // figure out which word is longer
        i = 0
        while i<index: 
            if i<len(word1):
                word += word1[i]
            if i<len(word2):
                word += word2[i]
            i += 1
        return(word)