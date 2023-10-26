# greatest common divisor of strings- runtime 30ms
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