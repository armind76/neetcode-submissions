/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL)
            return head;
        ListNode *res = head;
        ListNode *curr;
        ListNode *prev = NULL;
        while(res->next != NULL){
            curr = res;
            res = res->next;
            curr->next = prev;
            prev = curr;
        }
        res->next = prev;
        return res;
    }
};
