# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def printLL(self,head):
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        print ans
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        elif head.next is None:
            return TreeNode(head.val)
        else:
            #find the middle
            
            fast = head
            slow = head
            i = 0
            while fast.next is not None:
                if i%2 == 0:
                    prev = slow
                    slow = slow.next 
                fast = fast.next
                i+=1
            prev.next = None
            
            root = TreeNode(slow.val)
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(slow.next)
            return root

        