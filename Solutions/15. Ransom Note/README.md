# 15. Ransom Note [(LINK)](https://leetcode.com/problems/ransom-note)

> Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.


Solution:

* Given 2 strings, we need to check whether the count of number of alphabets in each string is same or not.
* This can be done using a counter, where if it reaches 0 for any character in the ransom note, we return false