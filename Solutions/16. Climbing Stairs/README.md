# 16. Climbing Stairs [(LINK)](https://leetcode.com/problems/climbing-stairs)

> You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Solution:

* To calculate the number of ways to climb the stairs, there are 2 options:
    * either we climbed one stair from the (n-1)th stair or
    * we climbed two stairs from the (n-2)th stair.
* By summing up the number of ways to reach the (n-1)th and (n-2)th stairs, we can compute the total number of ways to climb the stairs.