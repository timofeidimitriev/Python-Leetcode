# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize variables
        carry = 0
        head = ListNode()
        current = head
        
        # Loop until both lists are empty
        while l1 is not None or l2 is not None:
            # Calculate sum
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            
            # Update carry
            carry = sum // 10
            sum = sum % 10
            
            # Add node to linked list
            current.next = ListNode(sum)
            current = current.next
            
        # Add last digit if necessary
        if carry > 0:
            current.next = ListNode(carry)
            
        return head.next