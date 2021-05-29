##two sum two pointer way

'''s = [1,3,5,8,12,16,19]
k = 40
l,r = 0,len(s)-1
while l!=r:
    if s[l]+s[r]==k:
        print('GotEm')
        break
    elif s[l]+s[r]>k:
        r-=1
    elif s[l]+s[r]<k:
        l+=1
print('NotPsbl')
'''




##two sum sorted doubly linked list
# h,t = DoublylinkedList
  
#   2    3    6    8    12    15
#  h                            t

while h.val != t.val:
	if h.val + t.val == sum:
		return True
	elif h.val + t.val < sum:
		h = h.right
	elif h.val + t.val > sum:
		t = t.left
return False
