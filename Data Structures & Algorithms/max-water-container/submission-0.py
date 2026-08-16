class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            area = ((right - left) * min(heights[left], heights[right]))    
            if area > max:
                max = area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max
