class Solution:
    def numberToWords(self, num: int) -> str:
        ans = ''
        if num==0:
            return 'Zero'
        d = ['Trillion','Billion','Million','Thousand','']
        x= {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety',100:'Hundred',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',0:''}
        while num>0:
            newAns= ''
            newNum = num%1000
            num=num//1000
            unit = newNum%10
            newNum=newNum//10
            tens = newNum%10
            newNum = newNum//10
            hundred = newNum
            if hundred!=0:
                newAns = x[hundred]+ ' Hundred'
            if tens==1:
                newAns += ' ' + x[10+unit]
            else:
                newAns += ' ' + x[tens*10] + ' ' + x[unit]
            if newAns.strip() == '':
                d.pop()
                continue
            ans = newAns + ' ' + d.pop() + ' ' + ans
        return ' '.join([x for x in ans.split(' ') if x != ''])