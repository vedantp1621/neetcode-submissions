class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash 
        # o(1) l
        # 0(1) i

        # seen set

        seen = set()
        
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
            
        return False
        
        