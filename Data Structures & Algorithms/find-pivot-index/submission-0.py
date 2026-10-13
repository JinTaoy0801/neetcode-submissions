class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        
        lp = 0
        rp = 0

        for i in range(len(nums)):
            rp += nums[i]

        while l < len(nums):
            rp -= nums[l]
            if lp == rp:
                return l
            lp+=nums[l]
            l+=1





        return -1 