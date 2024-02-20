##  Leetcode week1-11

### https://leetcode.com/problems/balanced-binary-tree/description/
### Algorithm: Binary Search Tree


``` python
class Solution:
    def get_depth(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left, right = self.get_depth(node.left), self.get_depth(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left-right) >= 2:
            return -1
        return max(self.get_depth(node.left), self.get_depth(node.right))+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_depth(root) != -1:
            return True
        return False
```
