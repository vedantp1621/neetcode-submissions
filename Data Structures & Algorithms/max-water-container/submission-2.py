class Solution:
    def maxArea(self, heights: List[int]) -> int:
        print(heights)
        # must leave unsorted
        # track max seen height
        # only move the 'limiting' tower left or right

        left, right = 0, len(heights)-1
        max_height = 0

        while left < right:
            box = (right - left) * min(heights[left], heights[right])

            if box > max_height:
                max_height = box

            if heights[left] <= heights[right]:
                left += 1
                continue

            if heights[left] > heights[right]:
                right -= 1
                continue

        return max_height

            
        