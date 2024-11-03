# 18. Reverse Linked List [(LINK)](https://leetcode.com/problems/reverse-linked-list/)

> Given the head of a singly linked list, reverse the list, and return the reversed list.

Solution:

We maintain 3 pointers, curr, nxt and prev. All the events occur in a chain.
Preassign: prev = NULL and curr = head.

* First initialize nxt to be the node after curr. i.e nxt=cur->next .
* Then make cur->next point to prev (next node pointer).
* Then we make prev now point to (one node ahead) the curr node.
* At last we move curr also one node ahead to nxt.