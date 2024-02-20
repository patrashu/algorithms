##  Leetcode week2-4

### https://leetcode.com/problems/longest-palindrome/description/
### Algorithm: Dictionary

```python
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd_cnt = len(list(filter(lambda x: x[1]%2==1, counter.items())))
        if odd_cnt:
            return sum([k for k in counter.values()]) - odd_cnt + 1
        else:
            return sum([k for k in counter.values()]) 
```
