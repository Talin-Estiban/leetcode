#Best Time to Buy and Sell Stock
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Strategy:

First intuition:
- start the buy stock index as 0 which means the first day is the buy day and the profit as zero.
- we calculate the current profit as the substravtion between the maximum (sell day should be the maximum) of the list and the buy day. 
- update the profit value if the calculated profit (currentProfit) is larger than the actual profit.
- take the next list value as the new buy date and repeat the steps.

Second intuition:
- start the buy stock index as 0 which means the first day is the buy day and the profit as zero.
- this time we iterate through the sell date, such that if the sell date value is smaller than the buy date value we update the buy date such that the smaller the buy date value the better. Else we update the profit value.  
"""

#First intuition-  time limit exceded for very large lists
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        buyIndex=0
        while buyIndex<len(prices)-1:
            currentProfit= max(prices[buyIndex:])-prices[buyIndex]
            profit=max(profit,currentProfit)
            buyIndex+=1
        return profit

# Second intuition
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        buyPrice=prices[0]
        for price in prices:
            if price<buyPrice:
                buyPrice=price
            else:
                profit=max(profit,price-buyPrice)
        return profit
      