class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r_x = 0
        factor = 1
        negativeFlag = 1
        
        
        
        if x<0:
            x = -1 *x
            negativeFlag = -1
            
        while x>0:
            digit = x % 10
            r_x = r_x * 10 + digit
            x = x/10
        
        r_x = negativeFlag*r_x
        
        if r_x<-(2**31) or r_x>(2**31-1):
            return 0
        else:     
            return r_x
            
            
        