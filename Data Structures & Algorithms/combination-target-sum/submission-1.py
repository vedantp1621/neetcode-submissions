class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        sublist = []

        # sublist curr combination
        # i is index from nums
        # target is end goal
        # value is current value
        def dfs(sublist, i, value):
            if i >= len(nums):
                return
            if value > target:
                return
            if value == target:
                results.append(sublist.copy())
                return

            sublist.append(nums[i])
            dfs(sublist, i, value + nums[i])
            # check
            sublist.pop()
            # backtrack
            dfs(sublist, i+1, value)
            # check again

        dfs(sublist, 0, 0)
        return results