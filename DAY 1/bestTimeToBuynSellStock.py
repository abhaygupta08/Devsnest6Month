'''
Q - You are given array prices where price[i] is price of stock at day i 
You want to maximise profit by choose a single day to buy one stock and choosign a different day to sell the stock
Return the max profit ret 0 if not psbl
'''
prices = [7,1,5,3,6,4]

maxi = 0
for i in range(len(prices)):
	# print('i:',i)
	for j in range(i+1,len(prices)-i):
		# print('j:',j)
		# print('max:',maxi)
		# print(prices[j]-prices[i])
		if prices[j]-prices[i] > maxi:
			maxi = prices[j]-prices[i]
print(maxi) 

#---------or

minTillNow = 100000 #cause of constraint to prices in question
bestProfit = 0
for price in prices:
	if price < minTillNow:
		minTillNow = price
		# print('if ',end='')
	elif(bestProfit < (price-minTillNow)):
		bestProfit = (price-minTillNow)
	# 	print('elif ',end='')
	# print('minTillNow:',minTillNow,'price:',price,'bestProfit:',bestProfit,":::",price-minTillNow)
print(bestProfit)