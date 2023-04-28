from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = []
        n = list1
        while n is not None:
            list_1.append(n.val)
            n = n.next

        list_2 = []
        n = list2
        while n is not None:
            list_1.append(n.val)
            n = n.next

        for i in list_2:
            list_1.append(i)

        list_1.sort()

        # print(list_1)

        head = list1
        try:
            head = ListNode(list_1[0])
        except IndexError:
            return head
        tail = head
        e = 1
        while e < len(list_1):
            tail.next = ListNode(list_1[e])
            tail = tail.next
            e += 1
        return head
