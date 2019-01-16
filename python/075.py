class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = {0:0,1:0,2:0}
        for num in nums:
            count[num]+=1
        index = 0
        for j in count:
            while count[j]>0:
                count[j]-=1
                nums[index] = j
                index += 1
            