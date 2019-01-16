class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        len_nums = len(nums)
        if nums == []:
            return 1
        
        
        freq = range(1,len_nums+1)
        
        for i in nums:
            if i>0 and i<=len_nums:
                freq[i-1] += .1
        
        for j in range(1,len_nums+1):
            if j==freq[j-1]:
                return j
        
        return j+1