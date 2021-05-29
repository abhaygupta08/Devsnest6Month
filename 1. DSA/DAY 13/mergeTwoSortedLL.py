#NODE CREATION
class ListNode():
	def __init__(self,val=0,next=None):
		self.val = val
		self.next = next

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
	def addToFront(self,Elem):
		head = self
		n = ListNode(Elem)
		if not head:
			return n
		n.next = head
		return n
	def printLL(self):
		if not self:
			return None
		while self:
			print(self.val)
			self = self.next
	def deleteFirstNode(self):
		if not self:
			return None
		self = self.next
		return self
x = ListNode()

list1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
list2 = ListNode(2,ListNode(5,ListNode(7,ListNode(9))))

# list1.printLL()
# list2.printLL()

while list1 and list2:
	if list1.val < list2.val:
		x.addToEnd(list1.val)
		list1 = list1.next
	elif list1.val > list2.val:
		x.addToEnd(list2.val)
		list2 = list2.next
	elif list1.val == list2.val:
		x.addToEnd(list2.val)
		x.addToEnd(list1.val)
		list2,list1 = list2.next,list1.next
if list1:
	while list1:
		print('ADDED',list1.val)
		x.addToEnd(list1.val)
		list1 = list1.next
if list2:
	while list2:
		x.addToEnd(list2.val)
		list2 = list2.next

x = x.deleteFirstNode()
x.printLL()