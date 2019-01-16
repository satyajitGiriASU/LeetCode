class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        digit_char = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        list_combinations = []
        for digit in digits:
            # print(list_combinations)
            list_combinations = self.combine_2_strings(list_combinations,digit_char[digit])
        
        return list_combinations
    
    def combine_2_strings(self,list_str,str2):
        if list_str == []:
            ans = [char for char in str2]
        else:
            ans =  [str1+char for char in str2 for str1 in list_str]
        return ans
            
            