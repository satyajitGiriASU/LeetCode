class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] or nums is None:
            return 0
        
        unique_index = 0
        prev_unique_num = nums[unique_index]
        for i in range(1,len(nums)):
            if prev_unique_num == nums[i]:
                continue
            else:
                unique_index += 1
                nums[unique_index] = nums[i]
                prev_unique_num = nums[i]
        return unique_index+1
                    
        