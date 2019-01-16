class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        num_sign = 1
        first_nonwhitespace_flag = False
        x = 0
        
        for i in str:
            if not first_nonwhitespace_flag:
                if i != " ":
                    first_nonwhitespace_flag = True
                    if i == "-":
                        num_sign = -1
                    elif i == "+":
                        pass
                    else:
                        try:
                            digit = int(i)
                            x = x*10 + digit
                        except:
                            return 0
            else:
                try:
                    digit = int(i)
                    x = x*10 + digit
                except:
                    break
        if not first_nonwhitespace_flag:
            return 0
        else:
            x = num_sign* x
            if x > 2**31 -1:
                return 2**31-1 
            elif x<-2**31:
                return -2**31
            else:
                return x