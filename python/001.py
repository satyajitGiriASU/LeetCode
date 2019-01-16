class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        
        for ind, num in enumerate(nums):
            #The other number we need is sum of two numbers - current number
            if target-num not in hashtable:
                #if it's not there then add this number and it's index to the table
                hashtable[num]=ind
            else:
                #return the index of the current number and the index from hashtable
                return [hashtable[target-num],ind]