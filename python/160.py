# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        #Create a Hash Table
        hashTable = {}
        
        #Add each node in list A to the hashtable
        while headA is not None:
            hashTable[headA] = 1
            headA = headA.next
        
        #traverse through B until you find a node that was in A
        while headB is not None:
            if headB in hashTable:
                break
            else:
                headB = headB.next
        
        return headB