# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def printList(self,head):
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        print ans
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        slowPtr = head
        fastPtr = head
        
        i = 0
        while fastPtr is not None:
            if i%2 == 0:
                prevPtr = slowPtr
                slowPtr = slowPtr.next
            i += 1
            fastPtr = fastPtr.next
        
        prevPtr.next = None
        left_head = self.sortList(head)
        right_head = self.sortList(slowPtr)
        
        if left_head is None:
            return right_head
        elif right_head is None:
            return left_head
        else:
            if left_head.val < right_head.val:
                new_head = left_head
                left_head = left_head.next
            else:
                new_head = right_head
                right_head = right_head.next
                
        new_ptr = new_head
        
        while left_head is not None or right_head is not None:
            if left_head is None:
                new_ptr.next = right_head
                right_head = None
            elif right_head is None:
                new_ptr.next = left_head
                left_head = None
            elif left_head.val < right_head.val:
                new_ptr.next = left_head
                new_ptr = new_ptr.next
                left_head = left_head.next
            else:
                new_ptr.next = right_head
                new_ptr = new_ptr.next
                right_head = right_head.next
        return new_head
                
            
        
        

        