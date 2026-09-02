class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_val = 0

        # we are trying to get the maximum amount a container can store
        # have each pointer ref a bar, the pter that is pointing to the shorter bar can move inwards 

        while left < right:
            max_curr = min(heights[left], heights[right]) * (right-left)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            max_val = max(max_val, max_curr)

        return max_val




