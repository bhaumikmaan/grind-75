class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *curr = head,*prev = NULL,*next_node;
        while(curr!=NULL){
            next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        return prev;
    }
};