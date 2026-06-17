class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        infoPairs = {} # dict to store position:speed pairs for later analysis
        hours = [] # the stack that we will use to compare cars

        for i in range(len(position)): # iterate through each car 
            infoPairs[position[i]] = speed[i] # add a pair of pos:speed to the dict
        
        infoPairs = dict(sorted(infoPairs.items())) # sort this by furthest position
                                                    # to closest.
        # reasoning: since we will eventually build fleets of cars, we want to 
        # make sure we create a linear structure where the ones just starting
        # their journey are at the beginning and the ones closes to the end are
        # at the end of the list.
        
        # here, we calculate the 'speeds' by simplifying pos:speed into just the 
        # number of hours a car will take to reach. This is why its imporant to make
        # sure the car's index in the hours array reflects how far along it is, allowing
        # us to visualize blockages that will create fleets
        for pos,speed in infoPairs.items():
            hours.append((target-pos)/speed)

        numFleets = 1 # init fleet to one, since we have one train to begin with
        top = hours.pop() # take the top element for comparison
        while hours: # this loop will end once there are no cars left to compare
            if hours[-1] > top: # check if the top (current slow holdup car) has
                                # a slower car behind it that will not catchup
                numFleets+=1 # since it does, we will create a new fleet, assuming
                             # that the current top car will not be caught
                top = hours.pop() # the slower car at the front of the stack becomes
                                  # the new slow holdup car
            else: # otherwise, simply remove the next car, it will catchup to the 
                  # buildup car and we won't have to make a new fleet. The buildup
                  # car remains the same for future comparison
                hours.pop()
        
        return numFleets # return the number of fleets
