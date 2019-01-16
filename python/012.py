class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        factors = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romanChar = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        final_ans = ""
        currentFactorIndex = 0
        while num > 0:
            if num >= factors[currentFactorIndex]:
                final_ans += romanChar[currentFactorIndex]
                num -= factors[currentFactorIndex]
            else:
                currentFactorIndex += 1
        return final_ans