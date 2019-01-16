class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctoiMap = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500,"M":1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        val = 0
        i = 0
        length_string = len(s)
        while i < length_string:
            currentLetter = s[i]
            if currentLetter in ["I","X","C"] and length_string-i>1 and s[i:i+2] in ctoiMap:
                num = ctoiMap[s[i:i+2]]
                i += 2
            else:
                num = ctoiMap[currentLetter]
                i+=1
            val += num
        
        return val