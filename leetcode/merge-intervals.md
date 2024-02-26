##  Leetcode week5-4

### https://leetcode.com/problems/merge-intervals/description/
### Algorithm: sort

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = []
        i = 0

        while i < len(intervals):
            sv, ev = intervals[i]
            i += 1
            while i < len(intervals):
                if intervals[i][0] <= ev:
                    ev = max(ev, intervals[i][1])
                    i += 1
                else:
                    break
            ans.append([sv, ev])

        return ans
```
