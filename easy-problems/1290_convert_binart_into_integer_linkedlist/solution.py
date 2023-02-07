class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def counter(self, head):
        counter = 0
        while head is not None:
            counter += 1
            head = head.next
        return counter

    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        
        global decimelValue
        decimelValue = 0
        counterValue = self.counter(head) - 1
        while head is not None:
            if head.val == 0:
                counterValue = counterValue - 1
            else:
                decimelValue = decimelValue +  2 ** counterValue
                counterValue = counterValue - 1
            
            head = head.next
        return decimelValue