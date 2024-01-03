#Pascal's Triangle
"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Strategy:
- we know no matter the intered numRows the result has the list [1] so we start the result as [[1]].
- if the numRows is larger than 1 then we know we should append the next list [1,1]
- the remaining list items are created through the last list item.
- we know that all rows of pascal's triangle start and end in 1 and the middle values are figured through the previous list.
"""    
def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[[1]]
        if len(result)<numRows:
            result.append([1,1])
            index=1
            while len(result)<numRows:
                new=[1]
                for i in range(index):
                    new.append(result[-1][i]+result[-1][i+1])
                new.append(1)
                result.append(new)
                index+=1
        return result