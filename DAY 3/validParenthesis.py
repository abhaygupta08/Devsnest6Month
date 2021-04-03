arr1 = "[([]])"


'''
stackforParenthesis = []
for char in arr1:
	if char == '(':
		stackforParenthesis.append('(')
	elif char == '{':
		stackforParenthesis.append('{')
	elif char == '[':
		stackforParenthesis.append('[')
	if char == ')':
		if stackforParenthesis[-1] != '(':
			print('( ERROR ')
			exit()
		stackforParenthesis.remove('(')
	elif char == '}':
		if stackforParenthesis[-1] != '{':
			print('{ ERROR ')
			exit()
		stackforParenthesis.remove('{')
	elif char == ']':
		if stackforParenthesis[-1] != '[':
			print('[ ERROR ')
			exit()
		stackforParenthesis.remove('[')
	print(char+'',stackforParenthesis)
if len(stackforParenthesis):
	print('fail')
else:
	print('pass')
		
'''

stackforParenthesis = []
for char in arr1:
	if char in ['(','{','[']:
		stackforParenthesis.append(char)
	elif char in [')',']','}']:
		if not len(stackforParenthesis):
			exit('endingFirst')
		print(char)
		if char == ')': charOpening = '('
		if char == '}': charOpening = '{'
		if char == ']': charOpening = '['
		if stackforParenthesis[-1] != charOpening:
			exit('fail')
		stackforParenthesis.pop()
	print(char,stackforParenthesis)
if len(stackforParenthesis):
	print('fail')
else:
	print('pass')
		
