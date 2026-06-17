class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Create a hash table
        # [1,7,2,5,4,7,3,6] -> [1:0, 2:2, 3:6, 4:4, 5:3, 6:7, 7:1, 7:5]

        containers = []
        left, right = 0, len(heights) - 1

        while left < right:
            if heights[right] < heights[left]:
                containers.append((right - left) * (heights[right]))
                right -= 1
            else:
                containers.append((right - left) * (heights[left]))
                left += 1
            
        return max(containers)


