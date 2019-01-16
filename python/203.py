# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head is None:
            return None
        else:
            ans = ListNode(head.val)
            ptr = ans
            while head is not None:
                if head.val != val:
                    ptr.next = head
                    ptr = ptr.next
                head = head.next
            
            ptr.next = None
            return ans.next
            
            