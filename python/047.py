class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        
        len_nums = len(nums)
        
        if len_nums ==0:
            pass
        elif len_nums == 1:
            ans.append(nums)
        else:
            prev_numbers = []
            for i in range(len(nums)):
                curr_val = nums[i]
                if curr_val not in prev_numbers:
                    prev_numbers.append(curr_val)
                    rest_vals = nums[:i]+nums[i+1:]
                    
                    permutations = self.permuteUnique(rest_vals)
                    ans += [[curr_val]+p for p in permutations]
        
        return ans