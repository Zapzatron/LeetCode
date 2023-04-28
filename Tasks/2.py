from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = []
        n = l1
        while n is not None:
            list_1.append(n.val)
            n = n.next

        list_2 = []
        n = l2
        while n is not None:
            list_2.append(n.val)
            n = n.next

        list_1.reverse()
        list_2.reverse()

        num_1 = ""
        for num in list_1:
            num_1 += str(num)

        num_2 = ""
        for num in list_2:
            num_2 += str(num)

        # print(num_1, num_2)

        ans_list = str(int(num_1) + int(num_2))
        ans_list = [int(num) for num in ans_list]
        # print(ans_list)
        ans_list.reverse()
        # print(ans_list)
        try:
            head = ListNode(ans_list[0])
        except IndexError:
            return head

        tail = head
        e = 1
        while e < len(ans_list):
            tail.next = ListNode(ans_list[e])
            tail = tail.next
            e += 1
        return head
