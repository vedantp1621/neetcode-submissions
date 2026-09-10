class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        input: array sorted in asc order, now rotated between 1-n times

        two ptrs, one on each end. we move the smaller value inwards and keep track of a global min
        stop when the ptrs touch. -> this is a sub optimal two ptr approach that would be o(n)

        optimization: 
        '''

        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] >= nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]
