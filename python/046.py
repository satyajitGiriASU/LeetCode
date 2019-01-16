class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        else:
            answer = []
            for i in range(len(nums)):
                firstnum = nums[i]
                restnums = nums[:i]+nums[i+1:]
                returned_combinations = self.permute(restnums)
                answer += [[firstnum]+j for j in returned_combinations]
            return answer

                
                