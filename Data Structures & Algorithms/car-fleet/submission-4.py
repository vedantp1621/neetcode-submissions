class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        infoPairs = {}
        hours = []
        results = []

        for i in range(len(position)):
            infoPairs[position[i]] = speed[i]
        
        infoPairs = dict(sorted(infoPairs.items()))
        
        for pos,speed in infoPairs.items():
            hours.append((target-pos)/speed)

        print(hours)

        numFleets = 1
        
        top = hours[-1]
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
