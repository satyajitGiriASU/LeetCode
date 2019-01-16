class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        numMap = {}
        keys = []
        for i in nums:
            if i not in numMap:
                numMap[i] = 1
            else:
                numMap[i] += 1
        # print(sorted(numMap.values()))
        val = sorted(numMap.values())[-k]
        # print('val = ',val)
        soln = []
        
        count = 0
        for i in numMap:
            # print('i = ', i)
            # print('numMap[i] = ', numMap[i])
            if numMap[i]>= val:
                
                soln.append(i)
                count+=1
            if count >= k:
                break
        
        return soln
                