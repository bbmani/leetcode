def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    # IF BOTH OF THEM ARE NONE, WHICH MEANS THEY HAVE COME TO THE END OF THE Tree
    if not p and not q:
        return True
    # if one of them is empty, then the tree is not same 
    elif not p or not q:
        return False
    # if the node value is not the same, then it is not same tree 
    elif p.val != q.val:
        return False
    else:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)