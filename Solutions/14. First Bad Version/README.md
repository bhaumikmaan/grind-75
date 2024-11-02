# 14. First Bad Version [(LINK)](https://leetcode.com/problems/first-bad-version/)

> You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


Solution: 
* As we can see, the version history will be in a sorted order.
* Perform binary search and check whether the middle element is bad or not:
    * If it is bad means, a corrupt version exists before it
    * If it is not bad, it means corrupt version exists after it