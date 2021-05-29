class MinHeap():
	def __inti__(self,capacity):
		self.storage = [0]*capacity
		self.capacity = capacity
		self.size = 0
	
	def getParentIndex(self,index):
		return (index-1)//2
	def getLeftChildIndex(self,index):
		return (2*index)+1
	def getRightChildIndex(self,index):
		return (2*index)+2
	
	def hasParent(self,index):
		return self.getParentIndex(index) >=0
	def hasLeftChild(index):
		return self.getLeftChildIndex(index) < self.size
	def hasRightChild(index):
		return self.getRightChildIndex(index) < self.size

	def parent(self,index):
		return self.storage[self.getParentIndex(index)]
	def leftChild(self,index):
		return self.storage[self.getLeftChildIndex(index)]
	def rightChild(self,index):
		return self.storage[self.getRightChildIndex(index)]

	def isFull(self):
		return self.capacity==self.size
	def swap(self,index1,index2):
		self.storage[index1],self.storage[index2] = self.storage[index2],self.storage[index1]

	def insertMinHeap(self,data):
		if isFull(self):
			return False
		self.storage[self.size] = data
		self.size +=1
		self.heapifyUp(self,self.size-1)

	def heapifyUp(self,index):
		if self.hasParent(index) and self.parent(index) > self.storage[index]:
			self.swap(self.getParentIndex(index),index)
			self.heapifyUp(self.getParentIndex(index))

	def removeMinHeap(self):
		if self.size==0:
			return False
		data = self.storage[0]
		self.storage[0] = self.storage[self.size-1]
		self.size -=1
		self.heapifyDown(0)
	def heapifyDown(self,index):
		smallestChildInd = index
		if self.getLeftChildIndex(index) and self.storage[index] > self.leftChild(index):
			smallestChildInd = self.getLeftChildIndex(index)
		if self.hasRightChild(index) and self.storage[smallestChildInd] > self.rightChild(index):
				smallestChildInd = self.getRightChildIndex(index)
		if smallestChildInd ! =index:
			self.swap(index,smallestChildInd)
			self.heapifyDown(smallestChildInd)
		