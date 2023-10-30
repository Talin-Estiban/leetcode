#Reverse Vowels of  a String

# first intuition- time limit exceded passes 479/480 cases

def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=[]
        result=[]
        Vowels=["a","A","E","e","I","i","O","o","U","u"]
        for n in range(len(s)):# record places of vowels
            if s[n] in Vowels:
                vowels.append(n)
        org_vowels=vowels
        if vowels:# reverse vowels
            vowels=vowels[::-1]
        index=0
        for n in range(len(s)):# creating the result with the reversed vowels 
            result.append(s[n])
            if n in org_vowels:
                result[n]=s[vowels[index]]
                index+=1
        return "".join(result)