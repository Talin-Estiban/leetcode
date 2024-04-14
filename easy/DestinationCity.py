#Destination City

"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Strategy: 
- in my first submission, we see if the value is embedded in any other path. If not that means it's the destination. This didn't work becuase the arrays aren't sorted in any constant order.
- I created a dictionary that stores the value and the number of occurances of each one. The destibation city must have only one occurance and be placed at index 1 of the array. 
"""

#12/104 test cases passed

    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        result=""
        for n in range(len(paths)):
            if len(paths[n+1:])==0:
                return paths[n][1]
            else:
                for j in paths[n+1:]:
                    if paths[n][1] not in j:
                        result=paths[n][1]
                    else:
                        break

# all testcases passed:

    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        n={}
        for i in paths:
            for j in i: 
                if j in n:
                    n[j][0]+=1
                    n[j].append(i.index(j))
                else:
                    n[j]=[1,i.index(j)] 
        for key, value in n.items():
            if value==[1,1]:
                return key

