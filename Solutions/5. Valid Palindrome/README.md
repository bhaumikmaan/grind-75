# 5. Valid Palindrome [(LINK)](https://leetcode.com/problems/valid-palindrome/)

> Given a string s, return true if it is a palindrome, or false otherwise.

Condition: 
1. Remove all non-alphanumeric characters, 
2. Convert all uppercase letters into lowercase letters, check if it reads the same forward and backward


Solution: 

* Traverse the list using a `start` and `end` pointer till they cross each other
* For every non-alphanumeric element, just skip the element.
* If the characters are alphanumeric on both pointers, check whether their lowercase are same, if not return false.