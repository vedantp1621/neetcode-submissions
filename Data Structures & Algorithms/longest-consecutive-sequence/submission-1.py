class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        streaks_arr = []
        streaks_arr.append(0)
        streak = 0

        for num in nums:
            
            
            if not num-1 in nums_set:
                run = True
                streak += 1
                while run:
                    if num + streak in nums_set:
                        streak += 1
                    else:
                        run = False
                        streaks_arr.append(streak)
                        streak = 0

        return max(streaks_arr)

        