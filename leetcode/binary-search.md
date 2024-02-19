##  Leetcode week1-9

### https://leetcode.com/problems/binary-search/description/
### Algorithm: Binary Search


``` python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lidx, ridx = 0, len(nums)-1
        while lidx <= ridx:
            midx = (lidx+ridx)//2
            if nums[midx] == target:
                return midx
            elif nums[midx] > target:
                ridx -= 1
            else:
                lidx += 1

        return -1
```
