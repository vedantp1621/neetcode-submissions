class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # convert to hashset
        streaks_arr = [] # array of streak lengths
        streaks_arr.append(0) # default the set with element 0 (since were using max()
                              # we need to start with 0 so that the set is never empty)
        streak = 0 # initialize streak

        for num in nums: # iterate through num
            if not num-1 in nums_set: # use hashset function to make sure theres not a num 
                                      # 1 less than the num (better start of streak)
                run = True # start streak (since theres no better starting point)
                streak += 1 # count this num in streak
                while run: # runs until streak breaks
                    if num + streak in nums_set: # check if streak continues
                        streak += 1 # add to streak
                    else: # otherwise, break streak and add to streaks arr
                        run = False # break loop
                        streaks_arr.append(streak) # add to streaks arr
                        streak = 0 # reset streak

        return max(streaks_arr) # return the highest streak from all the streaks

        