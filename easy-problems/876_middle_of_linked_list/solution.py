# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def counter(self, head):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        
        return count

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        finalCount = self.counter(head)
        mid = finalCount / 2 if finalCount % 2 == 0 else math.ceil(finalCount / 2)
        print(mid)
        dummy = head

        while dummy is not None and mid != 0:
            dummy = dummy.next
            mid = mid - 1
        return dummy
    
        