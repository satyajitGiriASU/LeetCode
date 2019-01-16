class Solution(object):
            
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 =='0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '2':
            return num1
            
        s2i = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        
        len1 = len(num1)
        int1 = 0
        digit = 10**(len1-1)
        for i in num1:
            int1+=digit*s2i[i]
            digit/=10
            
        len2 = len(num2)
        int2 = 0
        digit = 10**(len2-1)
        for i in num2:
            int2+=digit*s2i[i]
            digit/=10
        
        int_ans = int1*int2
        i2s = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
        ans = ''
        
        while int_ans > 0:
            ans = i2s[int_ans%10]+ans
            int_ans /=10
        return ans