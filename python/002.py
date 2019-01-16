# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def ListNodeToNumber(l):
    n = l.val
    digit = 1
    while l.next is not None:
        digit *= 10
        l = l.next
        n = n+l.val*digit
    return n

def NumberToListNode(n):
    digit = n % 10
    node = ListNode(digit)
    n = n/10
    currentNode = node
    while n != 0:
        digit = n % 10
        currentNode.next = ListNode(digit)
        currentNode = currentNode.next
        n = n/10
    return node
    
    

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = ListNodeToNumber(l1)
        n2 = ListNodeToNumber(l2)
        sum_n = n1+n2
        return NumberToListNode(sum_n)
        
        