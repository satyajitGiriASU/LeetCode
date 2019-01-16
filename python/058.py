class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        inWordFlag = False
        lastWordLength = 0
        
        for i in s:
            if i == ' ' and inWordFlag:
                inWordFlag = not inWordFlag
            if i != ' ':
                if inWordFlag:
                    lastWordLength += 1
                else:
                    inWordFlag = not inWordFlag
                    lastWordLength = 1
        return lastWordLength