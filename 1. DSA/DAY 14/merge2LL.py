##merge
def MergeLists(list1, list2):
    if (list1 == None):
        return list2
    if (list2 == None):
        return list1
    if (list1.val < list2.val):
        list1.next = MergeLists(list1.next, list2)
        return list1
    else:
        list2.next = MergeLists(list2.next, list1)
        return list2
class Solution:
    def solve(self, ll0, ll1):
        return MergeLists(ll0,ll1)


##union
def MergeLists(list1, list2):
    if (list1 == None):
        return list2
    if (list2 == None):
        return list1
    if (list1.val < list2.val):
        list1.next = MergeLists(list1.next, list2)
        return list1
    elif (list1.val > list2.val):
        list2.next = MergeLists(list2.next, list1)
        return list2
    else:
        list1.next = MergeLists(list1.next, list2.next)
        return list1
class Solution:
    def solve(self, ll0, ll1):
        return MergeLists(ll0,ll1)