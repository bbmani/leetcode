def isSameTree(self, p, q):
    # FIRST CASE: if there is no left or right return true
    # SECOND CASE: if there is either left or right return false
    # THIRD CASE: if the values are not equal
    # recurse

    # BASE CASE
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
    
def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    
    p = root.left
    q = root.right

    return self.isSameTree(p,q)