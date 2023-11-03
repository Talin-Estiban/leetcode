#Roman to Integer
"""
Given a roman numeral s, convert it to an integer.  
Strategy:
- create a dictionary with the symbols and their values.
- itertae through s and check if the next symbol's value is smaller than the current symbols value. If yes
  then add the value to the result, and if not sybstract that from the result. 
* we check  the next symbol's value because in roman numbers they are written from the largest value to the smallest (from left to right).
But for example to write 4 in roman: IX = 5-1
  
"""
 def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        for i in range(len(s)-1):
            if x[s[i]]>=x[s[i+1]]:
                result+=x[s[i]]
            else:
                result-=x[s[i]]
        result+=x[s[len(s)-1]]
        
        return result
   