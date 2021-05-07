# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = []
        sortedLinkedList = ListNode("",)
        if l1:
            while l1 != None:
                l.append(l1.val)
                if l1.next == None:
                    l1 = None
                    break
                else:
                     l1 = l1.next
        if l2:
            while l2 != None:
                l.append(l2.val)
                if l2.next == None:
                    l2 = None
                    break
                else:
                    l2 = l2.next
        l.sort(reverse=True)
        for i in range(len(l)):
            if i == 0:
                sortedLinkedList = ListNode(l[i], None)
            else:
                sortedLinkedList = ListNode(l[i], sortedLinkedList)
        return sortedLinkedList