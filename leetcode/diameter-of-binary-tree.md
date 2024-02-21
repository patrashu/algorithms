##  Leetcode week2-8

### https://leetcode.com/problems/diameter-of-binary-tree/description/
### Algorithm: DFS, Tree

```python
class Solution:
    def __init__(self):
	    self.d = 0
	
    def depth(self, node: Optional[TreeNode]) -> int:
        # Calculate maximum depth
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        # Calculate diameter
        self.d = max(self.d, left + right)
        # Make sure the parent node(s) get the correct depth from this node
        return 1 + max(left, right)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.diameter
```
