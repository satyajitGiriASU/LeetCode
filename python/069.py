class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
        
        largest_ans = x
        smallest_ans = 1
        
        while True:
            current_ans = (largest_ans+smallest_ans)/2
            if current_ans*current_ans>x:
                largest_ans = current_ans -1
            else:
                if (current_ans+1)*(current_ans+1)>x:
                    return current_ans
                else:
                    smallest_ans = current_ans+1