class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums)==0:
            return 0
        else:
            start = 0
            end = len(nums)-1
            mid = (start+end)/2
            # print(start,mid,end)
            while (end-start)>2:
                print(nums[start],nums[mid],nums[end])
                if nums[mid]<target:
                    start = mid
                else:
                    end = mid
                mid = (start+end)/2
            print(nums[start],nums[mid],nums[end])
            
            if nums[start]>=target:
                return start
            elif nums[end]<target:
                return end+1
            elif nums[mid]<target:
                return mid+1
            else:
                return mid