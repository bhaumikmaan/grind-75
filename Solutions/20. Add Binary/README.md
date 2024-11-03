# 20. Add Binary [(LINK)](https://leetcode.com/problems/add-binary/)

> Given two binary strings a and b, return their sum as a binary string.

Solution:

* Initialize pointers for both strings starting from the end and use a variable to keep track of the carry.
* Iterate through both strings from the end to the start:
    * Sum the current digits of both strings along with the carry and update the carry.
    * Append the result to the output.
* After the loop, if there is any remaining carry, append it to the result.
* Reverse the result string since the digits were added from the least significant to the most significant.