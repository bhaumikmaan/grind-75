# 3. Merge Two Sorted Lists [(LINK)](https://leetcode.com/problems/merge-two-sorted-lists/)

> Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.


Solution: 

* Traverse the linked lists till both the lists have elements
    * Check which list has the smaller value, and add it to your answer
* Once one of the list is empty, appened the remaining other list to the answer.

