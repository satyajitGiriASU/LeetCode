class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length_largest_string = 0
        i = 0
        
        length_string = len(s)
        while(i<length_string):
            j = i + length_largest_string + 1
            
            if j <= length_string:
                substring = list(s[i:j])

                if len(substring)> len(set(substring)):
                    pass
                else:
                    length_largest_string = len(substring)

                    while(j<length_string):
                        new_char = s[j]
                        
                        if new_char not in substring:
                            substring.append(new_char)
                            
                            length_largest_string += 1            
                            j += 1
                        else:
                            
                            break
                    
            i+=1
        
        return length_largest_string