class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_brackets = []
        len_list = 0
        
        start_characters = ['(','{','[']
        end_characters = [')','}',']']
        start_end_mapping = {')':'(','}':'{',']':'['}
        
        for i in s:
            if i in start_characters:
                list_brackets.append(i)
                len_list += 1
            elif i in end_characters:
                if len_list:
                    last_bracket = list_brackets.pop()
                    if start_end_mapping[i] == last_bracket:
                        len_list -= 1
                    else:
                        return False
                else:
                    return False
        if len_list:
            return False
        else:
            return True