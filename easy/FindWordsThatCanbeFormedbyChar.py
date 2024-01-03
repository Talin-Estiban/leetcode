#Find Words That Can be Formed by Characters
"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.


Strategy:
- for every word in the list words:
	1. save chars into a list.
	2. start a flag variable called count that save the number of characters that are shared between chars and the word from words.
	3. compare between the variable count and the length of the word, if they are equal this means that all characters in the word is shared between it and chars.
"""
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result=0
        for word in words: #for every word in words
            char=[]
            char.extend(n for n in chars)# save chars into char as a list
            count=0
            for m in word:#iterate through characters in thw word
                if m in char:
                    char.remove(m)
                    count+=1
            if len(word)==count:
                result+=len(word)
        return result
