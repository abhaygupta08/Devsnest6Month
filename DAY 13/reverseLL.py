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
	def deleteLastNode(self):
		if not self:
			return None
		p = self
		while p.next.next:
			p = p.next
		p.next = None
		return self


head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
if not head:
	return None # in class resp
reversed = ListNode()

while head:
	reversed = reversed.addToFront(head.val)
	head = head.next

reversed = reversed.deleteLastNode()
reversed.printLL()
