# merge strings alternately

 # my first intuition- 30ms runtime
def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word=""
        length = len(word1)-len(word2)
        if length==0:
            for i in range(len(word1)):
                word += (word1[i]+word2[i])
        else:
            if length>0:
                for i in range(len(word2)):
                    word += (word1[i]+word2[i])
                word += word1[length:]
            else:
                for i in range(len(word1)):
                    word += (word1[i]+word2[i])
                word += word2[length:]
        return(word)

#second approach- 19ms runtime
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word = ""
        index = max(len(word1),len(word2))
        i = 0
        while i<index: 
            if i<len(word1):
                word += word1[i]
            if i<len(word2):
                word += word2[i]
            i += 1
        return(word)