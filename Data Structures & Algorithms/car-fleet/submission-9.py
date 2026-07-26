class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars going ->
        # we have the pos and the speed of each 
        # target miles 
        # car cant pass the car ahead

        # brute force: create a stack of cars in the fleet given that they all have the speed to do so
        # 


        # we cant use the stack to represent the fleet
        # make a list of cars that  will arrive at the same time

        # if a car is already closer to the target, cars behind cant pass it
        # convert the pos and speed into a third value, hours


        pair = [(p, s) for p, s in zip(position, speed)] # bring two arrays of info into one
        pair.sort(reverse=True) # sort by largest pos first, then speed

        # sorting technique to create a new array of pairs, with them
        # sorted in ascending order by position then speed. Means that top
        # element here will have the easiest positon to reach the target
        # why: we need some priority to process cars
        stack = []

        for p, s in pair: # iter through each pair
            stack.append((target-p)/s) # hour calculation
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # more than 1 elem to compare to
                                                           # remove this item from the stack if it is not 
                                                           # going to be the forerunner of a new fleet
                stack.pop()
        return len(stack)





        