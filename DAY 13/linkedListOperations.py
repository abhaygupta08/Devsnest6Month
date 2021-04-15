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
	def lengthOfLL(self):
		if not self:
			return 0
		count = 0
		while self:
			count +=1
			self = self.next
		return count
	def valueAt(self,index): ##index starts from zero
		if not self:
			return -1
		l = 0
		while self:
			if l == index:
				return(self.val)
			self = self.next
			l+=1
	def reverseLL(self):
		if not self:
			return -1
		temp = ListNode()
		while self:
			temp = temp.addToFront(self.val)
			self = self.next
		return temp.deleteLastNode()
	##TO DELETE
	def DeleteLast(self):
		if not self:
			return None
		p = self
		while p.next.next:
			p = p.next
		value = p.next.val
		p.next = None
		return self,value
	def DeleteFirst(self):
		if not self:
			return None
		return self.next,self.val
	def LLtoVal(self):
		if not self:
			return 0
		number = 0
		l = self.lengthOfLL()-1
		while self:
			number += 10**l * self.val
			self = self.next
			l-=1
		return number 
def valToLL(val):
	if val < 0 :
		return -1
	head = ListNode()
	for i in str(val):
		head = head.addToEnd(int(i))
	return head.deleteFirstNode()
l1 = ListNode(7,ListNode(2,ListNode(4,ListNode(3))))
l2 = ListNode(5,ListNode(6,ListNode(4)))

print(l1.LLtoVal() + l2.LLtoVal())
