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
    bool hasCycle(ListNode* head) {
        if(!head || !head->next)
            return false;
        ListNode* s = head;
        ListNode* f = head->next;
        while(f->next != NULL && f->next->next != NULL){
            if(f == s){
                return true;
                }
            s = s->next;
            f = f->next;
            f = f->next;
            
        }
        return false;
    }
};
