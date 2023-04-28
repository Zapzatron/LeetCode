from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        normal_list = []
        temp = lists.copy()
        for i in range(len(lists)):
            while temp[i] is not None:
                normal_list.append(temp[i].val)
                temp[i] = temp[i].next
        normal_list.sort()
        head = None
        try:
            head = ListNode(normal_list[0])
        except IndexError:
            return head
        tail = head
        e = 1
        while e < len(normal_list):
            tail.next = ListNode(normal_list[e])
            tail = tail.next
            e += 1

        return head
