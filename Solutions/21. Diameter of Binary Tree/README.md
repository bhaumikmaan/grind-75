# 21. Diameter of Binary Tree [(LINK)](https://leetcode.com/problems/diameter-of-binary-tree/)

> Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Solution:

* We find the maximum length string that we make to connect 2 endpoints
* That is done by finding max value of Height(leftSubtree) + Height(rightSubtree)(at any node) is the diameter.
* We find the maximum diameter during traversal and find the height of the tree.