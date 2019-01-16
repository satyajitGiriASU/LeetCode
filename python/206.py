# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #for empty lists
        if head is None:
            return None
        #for single length list
        elif head.next is None:
            return head
        #for multi node list:
        else:
            #Reverse the list except for the first number
            reversed_head = self.reverseList(head.next)
            #Make head.next (which is the last element of reversed list) point to head 
            head.next.next = head
            #Make smallest element(head) point to None
            head.next = None
            return reversed_head