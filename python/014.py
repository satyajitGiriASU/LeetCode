class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs)==1:
            return strs[0]
        else:
            prefix = strs[0]
            for j in range(1,len(strs)):
                new_word = strs[j]
                min_length = min(len(new_word),len(prefix))
                prefix = prefix[:min_length]
                new_word = new_word[:min_length]
                while min_length >= 0 :
                    if prefix == new_word:
                        break
                    else:
                        prefix=prefix[:-1]
                        new_word=new_word[:-1]
                        min_length -= 1
            return prefix