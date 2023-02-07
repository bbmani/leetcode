class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        revList = list()
        dummy = ListNode(0)
        while head is not None:
            revList.append(head.val)
            head = head.next
    
        revList = revList[::-1]
        temp = dummy
        for x in revList:
            temp.next = ListNode(x)
            temp = temp.next


        return dummy.next