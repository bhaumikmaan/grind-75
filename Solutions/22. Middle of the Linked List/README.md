# 22. Middle of Linked List [(LINK)](https://leetcode.com/problems/middle-of-the-linked-list/)

> Given the head of a singly linked list, return the middle node of the linked list.

Solution:

* While slow moves one step forward, fast moves two steps forward.
* When fast reaches the end, slow will be in the middle of the linked list.