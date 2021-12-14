class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(len(height)-1, i, -1):
                h1 = height[i]
                h2 = height[j]          
                w = abs(j - i)
                if h2 <= h1:
                    h = h2
                else:
                    h = h1
                a = w * h
                if a > max_area:
                    max_area = a
        return max_area
                