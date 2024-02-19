##  Leetcode week1-10

### https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
### Algorithm: Linked List, Tree


``` python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        if p.val <= root.val <= q.val:
            ans = root
        else:
            if root.left is not None and q.val < root.val:
                ans = self.lowestCommonAncestor(root.left, p, q)
            elif root.right is not None and root.val < p.val:
                ans = self.lowestCommonAncestor(root.right, p, q)
        
        return ans
```
