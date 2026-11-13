class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 # init pointers
        maxP=0 # base case

        while r < len(prices):
            #profitable
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP=max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP



            

        