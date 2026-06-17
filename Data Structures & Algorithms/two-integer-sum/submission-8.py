class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # will store visited values, storing as value:index

        for i, n in enumerate(nums): # enumerate: returns tuple of
                                     # (i = index, n = value)
            diff = target - n # use current iterated value and target
                              # to find value we're looking for in arr
                              # to complete pair
            if diff in prevMap: # since {} is a hash based container, we
                                # we can use 'in'
                return [prevMap[diff], i] # since we found the pair, return
            prevMap[n] = i # otherwise, add to visited