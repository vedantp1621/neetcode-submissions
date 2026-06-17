class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {} # holds the key:value pairs that show the frequency of each number in nums
        freq = [[] for i in range(len(nums) + 1)] # list of buckets, we will push values from nums into here
        for num in nums: # loop through nums, documenting frequencies of each number as key:value pairs
            counts[num] = 1 + counts.get(num, 0) # add one to each key
        for num, count in counts.items(): # loop through hash map
            freq[count].append(num) # in the bucket that corresponds to the value, add the key
        out = [] # holds the values that we will be returning
        for i in range(len(freq) - 1, 0, -1): # loops <- from k, up to 0, decrementing by 1
            for num in freq[i]: # loop through 
                out.append(num) # get the values of the most common keys
                if (len(out) == k): # stop once array is size of k
                    return out # return new list
            
        


        

            

            







