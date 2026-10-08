class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
            
        inc = True
        dec = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                inc = False
            if nums[i] < nums[i + 1]:
                dec = False
                
        return inc or dec