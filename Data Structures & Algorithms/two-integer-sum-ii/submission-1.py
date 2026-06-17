class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # sorted (l -> g)
        # returning 1 indexed list
        # two nums cannot be equal
        # must be in place
        # index1 must be < index2
        # given 'target'

        # numbers = [1,2,3,4], target = 3

        # left and right pointer
        # while loop ends when target is reached or pointers 
        # overlap

        # sum = left pointer num + right
        # compare sum to target
        # if sum >, move right pointer <- 
        # if sum is <, move left pointer -> 

        left, right = 0, len(numbers) - 1
        while left < right:
            sum_pointers = numbers[left] + numbers[right]

            if sum_pointers < target:
                left += 1
            elif sum_pointers > target:
                right -= 1
            elif sum_pointers == target:
                return [left+1, right+1]

        return []

