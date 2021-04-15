'''approach 1 

1. take first elem store then delete
2. take second elem store then delete
continue this untill list vanishes'''

'''#APPRACH 2
list = 1,2,5,8,9,11,13
if cen divide by half else take half+1 in l1
l1 = 1,2,5,8
l2 = 9,11,13
l2.rev = 13,11,9

l2 append continously to l1 e.g.  => 1 [13] 2 [11] 5 [9] 8'''


# CUTINHALF

# 2 pointer slow and fast

#    1 2 3 4 5 6
#    s f
#      s   f
#        s     f

#   s is mid if even length
#   else s+=1
#   

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def cutinhalf(head):
    fast,slow = head.next,head
    if not fast: ##one elem
        return head 
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    if fast.next:
        slow = slow.next
    k = slow.next
    slow.next = None
    return k
def reverse(head):
    if not head.next:
        return head
    p,c,n = head,head.next,head.next.next
    p.next = None
    while n:
        c.next = p
        p,c,n = c,n,n.next
    c.next = p
    return c

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: #len is 0 or 1 then
            return head
        h = cutinhalf(head)
        h = reverse(h)
        
        p = head
        while p and h:
            h2 = h.next
            h.next = p.next
            p.next = h
            
            p = p.next.next
            h = h2
        return head