word = "A man, a plan, a canal: Panama"
numeric,newstr,lowerCase,upperCase = [],[],[],[]
for i in range(97, 123):
  lowerCase.append(chr(i))
for i in range(65, 91):
  upperCase.append(chr(i))
for i in range(48,58):
  numeric.append(chr(i))
for let in word:
  if let in numeric or let in lowerCase or let in upperCase:
    newstr.append(let)

for i in range(len(newstr)):
  if newstr[i] in upperCase:
    newstr[i] = chr(ord(newstr[i])+32)
if newstr==newstr[::-1]:
  print('palindrme')
else:
  print('not plalindrome')