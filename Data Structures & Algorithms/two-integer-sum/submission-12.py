class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # rearange target s.t target - nums[i] = nums[j]
        # solve for nums[j]

        # first pass: put into dict: number: index

        nums_dictionary = {}

        for i in range(len(nums)):
            nums_dictionary[nums[i]] = i

 

        for i in range(len(nums)):
            output = []
            num_to_find = target - nums[i]

            if num_to_find in nums_dictionary and i != nums_dictionary[num_to_find]:
                output.append(i)
                output.append(nums_dictionary[num_to_find])
                return output




        