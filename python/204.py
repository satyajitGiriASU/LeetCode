class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return 0
        
        primeFlags = [True]*(n-2)
        
        for i in xrange(n-2):
            if not primeFlags[i]:
                continue
            else:
                primeNumber = i+2
                j = 2
                currentNumber = primeNumber*j 
                while currentNumber < n:
                    primeFlags[currentNumber-2] = False
                    currentNumber += primeNumber
        
        return sum(primeFlags)