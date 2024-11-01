class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxprofit = 0
        minpurchase = prices[0]
        
        for i in range(1 , len(prices)):
            mxprofit = max(mxprofit , prices[i] - minpurchase)
            minpurchase = min(prices[i] , minpurchase)
                
        return mxprofit