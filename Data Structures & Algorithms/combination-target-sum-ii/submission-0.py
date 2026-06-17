class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        sublist = []
        candidates.sort()

        def dfs(sublist, value, i):

            if value == target:
                results.append(sublist.copy())
                return
            if value > target or i >= len(candidates):
                return
            
            
            sublist.append(candidates[i])
            dfs(sublist, value + candidates[i], i+1)
            sublist.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(sublist, value, i+1)

        dfs(sublist, 0, 0)
        return results