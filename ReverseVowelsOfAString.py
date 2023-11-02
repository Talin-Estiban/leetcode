#Reverse Vowels of  a String
"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Strategy:
first intuition:
- iterate through the list and extract all vowels into a new list called vowels.
- reverse the extracted vowels.
- create a new list with the whole string and reversed vowels.

two pointers solution:
- convert the string into a list.
- iterate the list from the start and end and reverse vowels accordingly.

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

# two pointers - time limit exceded

       Vowels=["a","A","E","e","I","i","O","o","U","u"]
        sList = [n for n in s] # turn s into a list 
        n=len(sList)-1 # pointer from the end
        m=0 # pointer from the start of the list 
        while m<n:
            for i in range(m,n):
                if sList[i] in Vowels: #search for a vowel at the start of the list 
                    m+=1 #increment start index
                    for j in range(n,0,-1):
                        if sList[j] in Vowels:#search for a vowel at the end of the list 
                            n-=1 #increment end index
                            sList[i],sList[j]=sList[j],sList[i] #swap vowels 
                            break
        
        return "".join(sList)

# two pointers success 

def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        Vowels=["a","A","E","e","I","i","O","o","U","u"]
        sList = [n for n in s] # turn s into a list 
        n=len(sList)-1
        m=0
        while m<n:
            while m<n and sList[m] not in Vowels: # running from the start 
                m+=1
            while m<n and sList[n] not in Vowels:# running from the end
                n-=1
            sList[m],sList[n]=sList[n],sList[m] #swap vowels
            #increment indexes
            m+=1
            n-=1
        return "".join(sList)