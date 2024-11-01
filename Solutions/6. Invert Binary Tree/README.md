# 6. Invert Binary Tree [(LINK)](https://leetcode.com/problems/invert-binary-tree/)

> Given the root of a binary tree, invert the tree, and return its root.

Note: It is a binary tree: A tree in which each node has at most two children.

Solution: 

* Base Case: Check if the root is `NULL`. This means the parent was a leaf node and now there are no more nodes to access.
* Swap Left and Right Children. By swapping the children and recursively repeating the process, we essentially swap the entire binary tree
* After swapping the current node children, we recursively invert the left subtree and right subtree