# merge strings alternately

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