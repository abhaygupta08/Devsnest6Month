'''
THEORY

[1.]
class Lion():
	pass

x = Lion()

print(type(x)) ===> class Lion


[2.]
w/ Constructor

class Lion():
	def __init__(self):
		self.ht = 12
		self.wt = 3
		self.name = 'Abhay'

[3.]
Linked list traversal is o(n) operation
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



'''



'''
class main():
	def __init__(self):
		self.name = 'Abhay'
		self.wt = 12
x = main('Raaam',22)
print(x.name,x.wt)

'''
'''
class main():
	def __init__(self,nm,wei=12):
		self.name = nm
		self.wt = wei
x = main('name')
print(x.name,x.wt)

'''
'''
class main():
	def __init__(self,nm):
		self.name = nm
	def tellYourName(self,ysy):
		print(self.name)
		print(ysy)



if __name__=="__main__":
	x = main('HELLO')
	print(x.name)
	x.tellYourName('random')

'''


##LINKED LIST
class ListNode:
	def __init__(self,val,nextr=None):
		self.val = val
		self.next = nextr

head = ListNode('1stNode',ListNode('2ndNode',ListNode('3rdNode')))

def PrintLinkedList(head):
	while head:
		print(head.val)
		head = head.next

def InsertAtLast(head,Elem):
	n = ListNode(Elem,None)
	p = head
	if not head:
		return n
	while p.next:
		p = p.next
	p.next = n
	return head

def InsertAtFront(head,Elem):
	n = ListNode(Elem,None)
	n.next = head  # head=none if list is empty else head points to 1st element
	return n

## Delete kth elem starting from zero
def DeleteAtkPos(head,k):
	if k == 0:
		return head.next
	p = head
	while k > 1:
		k -= 1
		p = p.next
	p.next = p.next.next
	return head

head = InsertAtLast(head,'4thNode')
PrintLinkedList(head)

print('\n')

head = InsertAtFront(head,'0thNode')
PrintLinkedList(head)

print('\n')

head = DeleteAtkPos(head,5)
PrintLinkedList(head)