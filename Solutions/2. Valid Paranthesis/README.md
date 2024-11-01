# 2. Valid Parentheses [(LINK)](https://leetcode.com/problems/valid-parentheses/)

> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


Conditions of validity:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


Solution: 

* Opening bracket closed in correct order means when a bracket is opened, that bracket should be closed first.
* Base Case: If length of string is odd, the string is invalid
* For each opening bracket, add it to the stack.
* For each closing bracket, check the top of the stack to find its opening bracket. If not found, it is invalid.
