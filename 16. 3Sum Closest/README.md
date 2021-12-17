# 16. 3Sum Closest

## Successful Attempts: 0

## Failed Attempts: 1

## Notes
This is a tricky one for me. I can solve relatively easily with O(n^3), but I know it's possible and have only tried to solve with O(n^2)

Here is the O(n^2) python solution from leetcode comments section

```
def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float('inf')
        ans = 0
        l = len(nums)
        
        nums.sort()
        for i in xrange(l):
            lo = i + 1
            hi = l - 1
            
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                d = abs(target - s)
                if d == 0:
                    return s
                if d < diff:
                    diff = d
                    ans = s
                if s < target:
                    lo += 1
                else:
                    hi -= 1
        return ans
```