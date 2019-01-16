class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        
        if len(s) != len(t):
            return False
        
        if len(s) == 0:
            return True
        
        isomorphicFlag = True
        charMap = {}
        
        for i,j in zip(s,t):
            if i in charMap:
                if charMap[i] == j:
                    continue
                else:
                    isomorphicFlag = False
                    break
            else:
                if j not in charMap.values():
                    charMap[i] = j
                else:
                    isomorphicFlag = False
                    break
        
        return isomorphicFlag