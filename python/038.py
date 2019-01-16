class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return '1'
        else:
            prevWord = self.countAndSay(n-1)
            #prevWord = 11
            finalWord = ''
            
            count = 0
            prevLetter = prevWord[0]
            for i in prevWord:
                if i!= prevLetter:
                    finalWord += (str(count)+prevLetter)
                    count = 1
                    prevLetter = i
                else:
                    count+=1
            finalWord += (str(count)+prevLetter)
            return finalWord