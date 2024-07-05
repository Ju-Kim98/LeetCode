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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        ListNode* pre = head;
        ListNode* cur = head -> next;
        
        vector<int> res = {-1,-1};
        
        int prePos = -1, curPos = -1, firstPos = -1, pos = 0;
        while(cur -> next != NULL) {
            if((cur -> val<pre -> val&&cur -> val<cur -> next -> val) || (cur -> val>pre -> val &&cur -> val>cur -> next -> val)) {
                //local
                prePos = curPos;
                curPos = pos;
                if(firstPos == -1){
                    firstPos = pos;
                }
                if(prePos != -1) {
                    if(res[0] == -1) res[0] = curPos - prePos;
                    else res[0] = min(res[0], curPos - prePos);
                    res[1] = pos - firstPos;
                }
            }
            pos++;
            pre = cur;
            cur = cur -> next;
        }
        
        return res;
    }
};