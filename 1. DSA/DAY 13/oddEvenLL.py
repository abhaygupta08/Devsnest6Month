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

oddLL = ListNode()
evenLL = ListNode()

head = ListNode(2,ListNode(1,ListNode(3,ListNode(5,ListNode(6,ListNode(4,ListNode(7)))))))
index = 0
while head:
	if index%2 == 0:
		evenLL.addToEnd(head.val)
	elif index%2 == 1:
		oddLL.addToEnd(head.val)
	index+=1
	head = head.next

evenLL = evenLL.deleteFirstNode()
oddLL = oddLL.deleteFirstNode()

while oddLL:
	evenLL.addToEnd(oddLL.val)
	oddLL = oddLL.next
evenLL.printLL()