height = [1,2,1]
N,maxArea = len(height),0
s,e = 0,N-1
while s<e:
	w = s-e
	if w < 0:
		w = -w
	h = min(height[s],height[e])
	areaTemp = w*h
	if areaTemp > maxArea:
		maxArea = areaTemp
		print(height[s],height[e])
	if height[s]>height[e]:
		e -= 1
	elif height[s]<height[e]:
		s += 1
	elif height[s]==height[e]:
		e -= 1
		s += 1
print(maxArea)