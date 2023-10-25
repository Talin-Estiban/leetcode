# greatest common divisor of strings- runtime 30ms
def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1)>len(str2):
            base = str2
            word=str1
        else:
            base = str1
            word = str2
        for i in range(len(base)):
            length = len(word) / len(base)
            sample=""
            for j in range(length):
                sample += base
            if sample==word:
                return(base)
            else:
                base = base[:-1]
        return("")