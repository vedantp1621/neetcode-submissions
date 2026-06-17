class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        # create len(nums) buckets
        # 

        buckets = [[] for i in range(len(nums) + 1)]
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        for key, value in count.items():
            buckets[value].append(key)

        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
                

                

 



        print(bucket)

