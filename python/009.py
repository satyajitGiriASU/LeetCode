class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        origNo = x
        if x < 0:
            return False
        else:
            str_x = str(x)
            last_ind = len(str_x) - 1
            start_ind = 0
            while last_ind > start_ind:
                if str_x[start_ind] != str_x[last_ind]:
                    return False
                start_ind += 1
                last_ind -= 1
            
            return True