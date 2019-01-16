class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hash_s = {}
        hash_t = {}
            
        if len(s)!=len(t):
            return False
        
        for a,b in zip(s,t):
            if a not in hash_s:
                hash_s[a]=0
            if b not in hash_t:
                hash_t[b]=0
            
            hash_s[a]+=1
            hash_t[b]+=1
        return hash_s == hash_t