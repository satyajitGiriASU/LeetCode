# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        num_elem = len(nums)
        
        if num_elem == 0:
            return None
        elif num_elem == 1:
            return TreeNode(nums[0])
        else:
            mid_index = num_elem/2
            head = TreeNode(nums[mid_index])
            head.left = self.sortedArrayToBST(nums[:mid_index])
            head.right = self.sortedArrayToBST(nums[mid_index+1:])
            return head
            
            
            