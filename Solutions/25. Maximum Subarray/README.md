# 25. Maximum Subarray [(LINK)](https://leetcode.com/problems/maximum-subarray/)

> Given an integer array nums, find the subarray with the largest sum, and return its sum.

Solution: **Kadane's Algorithm**

* We need to maintain `curMax` which is the maximum subarray sum ending at `i`. 
    * This means that it stores the sum of the current subarray
    * Or it starts a new subarray, depending on which is greater
* We store the maximum value of `curMax` which is our answer