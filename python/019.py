# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodetoberemoved = head
        endnode = head
        
        if not n:
            return head
        #since n is valid, setup
        for i in range(n-1):
            endnode = endnode.next
        
        #if we have to remove first node
        if endnode.next is None:
            return head.next
        else:
            while endnode.next is not None:
                prevNode = nodetoberemoved
                nodetoberemoved = nodetoberemoved.next
                endnode = endnode.next
            
            prevNode.next = nodetoberemoved.next
            return head
                
            
            
        