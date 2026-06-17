class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:  
        left, right = 0, len(numbers) - 1

        print(left)
        print(right)

        while left < right:
            correctpair = target - numbers[left]
            if numbers[right] > correctpair:
                right -= 1
                continue
            elif numbers[right] < correctpair:
                left += 1
                continue
            if numbers[left] + numbers[right] == target:
                break

        return[left + 1, right + 1]



    # increasing
    # one-indexed -> starts at 1

    # [2,4,6,8,10] target = 14 

    # left = 0
    # right = 4
    # target - left = 12
    # left has to go up since right is max and it is 10
    
    # left = 1
    # right = 4
    # target - left = 10
    # found -> 4+10 = 14

    # [1,2,3,4] target = 3
    
    # left = 0
    # right = 3
    # target - left = 2
    # right has to go down since it is 4 which would exceed the target

    # left = 0
    # right = 2
    # target - left = 2
    # right has to go down same reason

    # left = 9
    # right = 1
    # target - left = 2
    # right = 2 so its good