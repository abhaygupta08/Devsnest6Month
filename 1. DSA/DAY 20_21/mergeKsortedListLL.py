# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists==[None] or len(lists)==0:
            return None
        temp = []
        for i in lists:
            while i:
                temp.append(i.val)
                i = i.next
        temp.sort()
        if len(temp)==0:
            return None
        s = ListNode(temp[0])
        m = s 
        for i in range(1,len(temp)):
            n = ListNode(temp[i])
            s.next = n
            s = s.next
        return m

##DEVS APPROACH

import heapq

class Solution:
    def mergeKLists(self, lists:List[ListNode]) -> ListNode:
        setattr(ListNode,"__it__",lambda self,other:self.val <= other.val)
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap,head)
        ans = ListNode(None)
        p = ans

        while len(heap)>0:
            n = heapq.heappop(heap)
            p.next = n
            p=n
            if n.next:
                heapq.heappush(heap,n.next)
        return ans.next