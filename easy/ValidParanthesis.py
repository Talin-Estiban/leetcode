#Valid Paranthesis
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.
3.Every close bracket has a corresponding open bracket of the same type.

Strategy:
- add every open paranthesis into the list o.
- if the paranthesis is a closing one we compare it to the last paranthese in the last, if they match delete 
  the open one from the list.if it's not then the string given is not valid and return false.
- if there's any parantheses left in the o list then the string given is not valid and return false.
"""
def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbols={"(":")","[":"]","{":"}"}
        o=[] #list to store open paranthesis 
        for i in s:
            if i in symbols.keys():# store open paranthesis 
                o.append(i)
            else:
                if not o or i!=symbols[o[-1]] :
                    return False
                else:
                    o.pop()
        return not o
                   