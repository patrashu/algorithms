##  Leetcode week5-6

### https://leetcode.com/problems/time-based-key-value-store/description/
### Algorithm: Hash

```python
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.k_to_v = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.k_to_v[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        candit = self.k_to_v[key]
        l, r = 0, len(candit)-1
        while l <= r:
            m = (l+r)//2
            if timestamp < candit[m][1]:
                r = m-1
            else:
                l = m+1
        return "" if r == -1 else candit[r][0]
```
