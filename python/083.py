# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        else:
            prevptr = head
            currptr = head.next
            
            while currptr is not None:
                if prevptr.val == currptr.val:
                    prevptr.next = currptr.next
                else:
                    prevptr = currptr
                
                currptr = currptr.next
            return head
        
       
            
        