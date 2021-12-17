import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_dist = sys.maxsize
        closest_sum = None
        for i in range(len(nums)):
            pointer_val1 = nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                elif j + 1 == i:
                    continue
                elif j + 1 > len(nums) - 1:
                    break
                else:
                    pointer_val2 = nums[j]
                    pointer_val3 = nums[j+1]
                    sum_ = pointer_val1 + pointer_val2 + pointer_val3
                    if abs(sum_ - target) < closest_dist:
                        closest_dist = abs(sum_ - target)
                        closest_sum = sum_
        return closest_sums