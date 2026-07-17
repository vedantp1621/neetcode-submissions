class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # left ptr and right ptr 
        # left is small right is big
        # if left+right too small, push left
        # if left+right too big, pull right

        left, right = 0, len(numbers)-1
        results = []
        while left < right:
            curr = numbers[left] + numbers[right]
            
            # push leftt
            if curr < target:
                left+=1
                continue
            # pull right
            if curr > target:
                right-=1
                continue
            if curr == target:
                results.append(left+1)
                results.append(right+1)
                break

        return results


        