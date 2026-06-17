class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # returning array
        # nums[i] + nums[j] == target
        # target - nums[i] == nums[j]

        # hash map

        # add entire array to hashmap
        # key:val pair is the num:index

        #iterate through original array, check if in hashmap

        results = []
        num_map = {}

        for i in range(len(nums)):
            num_map[nums[i]] = i

        for i in range(len(nums)):
            results = []
            pair_target = target - nums[i]
            if pair_target in num_map and num_map[pair_target] != i:
                results.append(min(i, num_map[pair_target]))
                results.append(max(i, num_map[pair_target]))
                break
            

        return results






