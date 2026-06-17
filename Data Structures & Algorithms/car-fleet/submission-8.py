class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars going ->
        # we have teh pos and the speed of each 
        # target miles 
        # car cant pass the car ahead

        # brute force: create a stack of cars in the fleet given that they all have the speed to do so
        # 


        # we cant use the stack to represent the fleet
        # make a list of cars that  will arrive at the same time

        # if a car is already closer to the target, cars behind cant pass it
        # convert the pos and speed into a third value, hours


        pair = [(p, s) for p, s in zip(position, speed)] # sort by position, then speed
        pair.sort(reverse=True) # largest first
        stack = []

        for p, s in pair:
            stack.append((target-p)/s) # calcs the hours from pos to target
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # found some seperation in arrivals
                stack.pop()
        return len(stack)





        