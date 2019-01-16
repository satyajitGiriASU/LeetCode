class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seenNumbers = [n]
        while True:
            newNumber = 0
            while n>0:
                newNumber += (n%10)**2
                n = n/10
            if newNumber == 1:
                return True
            elif newNumber in seenNumbers:
                return False
            else:
                seenNumbers.append(newNumber)
                n = newNumber
        