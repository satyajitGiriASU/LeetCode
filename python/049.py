class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dict_anagram = {}
        
        for word in strs:
            key = sorted(word)
            key = ('').join(key)
            if key not in dict_anagram:
                dict_anagram[key] = [word]
            else:
                dict_anagram[key].append(word)
            
        return dict_anagram.values()
                