class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        maxvol = 0
        
        while True:
            if i>=j:
                break
            
            hi = height[i]
            hj = height[j]
            if (hi<hj):
                vol = hi*(j-i)
                i+=1
            else:
                vol = hj*(j-i)
                j-=1
            
            if maxvol<vol:
                maxvol = vol
        return maxvol
            
            