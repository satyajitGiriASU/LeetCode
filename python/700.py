# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        ptr = root
        
        while ptr is not None:
            if ptr.val == val:
                return ptr
            elif val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return None
        