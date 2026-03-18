class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        l = 0
        r = n-1
        max_area = 0

        while l<r:
            h = min(heights[l], heights[r])
            w = r-l
            a = h*w
            print(a)
            max_area = max(a, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        