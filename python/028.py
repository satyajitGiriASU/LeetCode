class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == '':
            return 0
        elif haystack == '':
            return -1
        else:
            needle_len = len(needle)
            for i in range(0,len(haystack)-needle_len+1):
                if haystack[i:i+needle_len] == needle:
                    return i
            
            return -1