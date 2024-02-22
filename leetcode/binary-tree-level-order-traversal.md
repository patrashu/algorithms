##  Leetcode week3-6

### https://leetcode.com/problems/binary-tree-level-order-traversal/description/
### Algorithm: BFS, Tree

```python
from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = defaultdict(list)
        dq = deque([(root, 0)])
        m_depth = 0
        while dq:
            node, depth = dq.popleft()
            ans[depth].append(node.val)
            m_depth = max(m_depth, depth)
            if node.left:
                dq.append((node.left, depth+1))
            if node.right:
                dq.append((node.right, depth+1))                    

        return [k[1] for k in sorted(ans.items(), key=lambda x: x[0])]
```
