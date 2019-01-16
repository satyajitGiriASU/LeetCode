# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        i = 0
        slow = head
        fast = head
        while fast.next is not None:
            if i%2 == 0:
                prev = slow
                slow = slow.next
            fast = fast.next
            i+=1
        
        return slow