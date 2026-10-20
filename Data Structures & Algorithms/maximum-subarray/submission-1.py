class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        total = 0
        m = nums[0]
        for i in range(len(nums)):
            total+=nums[i]
            if total < 0:
                m = max(m,total)
                total = 0
                
                continue
            
            m = max(m,total)

        return m
