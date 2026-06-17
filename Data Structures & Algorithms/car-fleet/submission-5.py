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
        top = hours.pop()
        while hours:
            if hours[-1] > top:
                numFleets+=1
                top = hours.pop()
            else:
                hours.pop()
        
        return numFleets


# target = 10
# pos = [0,1,4,7] speed = [1,2,2,1]
# [[10], [4.5], [3, 3]]

# target = 10
# position = [1,4], speed = [3,2]
# [[3,3]]

# Plan of action
# Create dict of position:speed
# Sort positions array least to greatest
# Create hours array by hours = (target - postion) / speed
# Use stack to build groups based on if the prev hours is <= curr
