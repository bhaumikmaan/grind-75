# 4. Best Time to Buy and Sell Stock [(LINK)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

> You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return: The `maximum profit` you can achieve from this transaction. If you cannot achieve any profit, return `0`.



Solution: 

* Store the minimum purchase value of any stock using a variable `mn`
* For every element, find the maximum profit  `mx`, that can be gained by selling it at the point, from buying at minimum price `mn`.