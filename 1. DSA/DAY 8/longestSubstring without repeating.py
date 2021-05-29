s = 'abcabcbb'
ans,l,r,chararraay = 0,0,0,set()
while(r<len(s)):
	if s[r] in chararraay:
		while s[l]!=s[r]:
			l+=1
		l+=1
	else:
		chararraay.add(s[r])
		print(chararraay,l,r)
		if ans < len(chararraay):
			ans = len(chararraay)
	r+=1
print(ans)