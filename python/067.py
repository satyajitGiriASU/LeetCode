class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        carry = '0'
        
        len_a = len(a)
        len_b = len(b)
        
        if len_a > len_b:
            b = (len_a-len_b)*'0'+b
        if len_b > len_a:
            a = (len_b-len_a)*'0'+a
        
        c = ''
        for i in range(max(len_a,len_b)-1,-1,-1):
            if a[i] == '0' and b[i] == '0' and carry == '0':
                c = '0' + c
                carry = '0'
            elif (a[i] == '1' and b[i] == '0' and carry == '0') or (a[i] == '0' and b[i] == '1' and carry == '0') or (a[i] == '0' and b[i] == '0' and carry == '1'):
                c = '1' + c
                carry = '0'
            elif (a[i] == '1' and b[i] == '1' and carry == '0') or (a[i] == '0' and b[i] == '1' and carry == '1') or (a[i] == '1' and b[i] == '0' and carry == '1'):
                c = '0' + c
                carry = '1'
            else:
                c = '1' + c
                carry = '1'
        
        if carry == '1':
            return carry+c
        else:
            return c
                
            
        
        