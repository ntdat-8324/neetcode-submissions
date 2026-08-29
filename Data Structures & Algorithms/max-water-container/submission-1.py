class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_a = 0
        while i < j:
            min_h = min(heights[i], heights[j])

            area = min_h * (j-i)

            if area > max_a:
                max_a = area
            
            if heights[i] < heights[j]:
                i += 1
            else: j -= 1

        return max_a