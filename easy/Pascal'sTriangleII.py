#Pascal's Triangle II
"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Strategy:
- we know no matter the intered numRows the result has the list [1] so we start the result as [[1]].
- if the numRows is larger than 1 then we know we should append the next list [1,1]
- the remaining list items are created through the last list item.
- we know that all rows of pascal's triangle start and end in 1 and the middle values are figured through the previous list.
- the rowIndex list is the last list in the result.
"""  
def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        answer=[[1]]
        if rowIndex>0:
            answer.append([1,1])
            index=1
            while len(answer)<(rowIndex+1):
                new=[1]
                for i in range(index):
                    new.append((answer[-1][i]+answer[-1][i+1]))
                new.append(1)
                index+=1
                answer.append(new)
        print (answer)
        return answer[-1]