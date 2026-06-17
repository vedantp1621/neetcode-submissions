class TimeMap:


    # store in a dict for fast lookup
    # key: [value, timestamp]
    def __init__(self):
        self.keyStore = {}
        
    # if the key is not in the dict, create new empty bucket 
    # append to the key, a sublist of [value, timestamp]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        
    # how to make search faster:
    # given key, given timestamp    
    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # this means that we look in right sublist
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

        
