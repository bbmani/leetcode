class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)

    currNode = head
    finalList = list()

    while currNode is not None:
        if currNode.val not in finalList:
            finalList.append(currNode.val)
        currNode = currNode.next

    temp = dummy
    for x in finalList:
        temp.next = ListNode(x)
        temp = temp.next
    
    return dummy.next