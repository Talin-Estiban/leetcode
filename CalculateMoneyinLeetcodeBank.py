# Calculate Money in Leetcode Bank
"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Strategy:
- while the days we calculated is smaller than n, for every week we save starting on the minimum that is the number of mondays that have passed.
"""
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        days=0
        money=0
        numMondays=0
        while days<n:
            numMondays+=1
            for m in range(numMondays,(7+numMondays)):
                money+=m
                days+=1
                if days==n:
                    return money
        return money
