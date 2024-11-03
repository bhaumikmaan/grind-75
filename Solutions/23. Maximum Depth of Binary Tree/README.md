# 23. Maximum Depth of Binary Tree [(LINK)](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

> Given the root of a binary tree, return its maximum depth.

Solution:

* Max depth means the number of nodes along the longest path from root to farthest leaf node.
* For each level, we need to find how deep the subtree goes. 
* We can do this recursively by having a depth counter that checks the max depth of each subtree