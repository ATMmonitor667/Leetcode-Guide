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
    ListNode* mergeTwo(ListNode* one, ListNode* two) {
        ListNode dummy(0);
        ListNode* cursor = &dummy;

        while (one && two) {
            if (one->val <= two->val) {
                cursor->next = one;
                one = one->next;
            } else {
                cursor->next = two;
                two = two->next;
            }
            cursor = cursor->next;
        }

        cursor->next = one ? one : two;
        return dummy.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        while (lists.size() > 1) {
            vector<ListNode*> merged;
            merged.reserve((lists.size() + 1) / 2);

            for (int i = 0; i < (int)lists.size(); i += 2) {
                ListNode* one = lists[i];
                ListNode* two = (i + 1 < (int)lists.size()) ? lists[i + 1] : nullptr;
                merged.push_back(mergeTwo(one, two));
            }

            lists = std::move(merged);
        }

        return lists[0];
    }
};
