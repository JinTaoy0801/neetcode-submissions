class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        total = 0
        m = nums[0]
        for i in range(len(nums)):
            
            if total < 0:
                total = 0         
            
            total+=nums[i]
            m = max(m,total)

        return m
