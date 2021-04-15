# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def lengthOfLL(self):
        if not self:
            return 0
        count = 0
        while self:
            count +=1
            self = self.next
        return count
    def deleteFirstNode(self):
        if not self:
            return None
        self = self.next
        return self
    def addToEnd(self,Elem):
        head = self
        n = ListNode(Elem)
        if not head:
            return n
        p = head
        while p.next:
            p = p.next
        p.next = n
        return head
	

def LLtoVal(head):
    if not head:
        return 0
    number = 0
    p = head
    len = 0
    while p:
        len +=1
        p = p.next
    l = len-1
    while head:
        number += 10**l * head.val
        head = head.next
        l-=1
    return number
    
def valToLL(val):
    if val < 0 :
        return -1
    head = ListNode()
    for i in str(val):
        head = head.addToEnd(int(i))
    return head.deleteFirstNode()

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return valToLL(LLtoVal(l1) + LLtoVal(l2))