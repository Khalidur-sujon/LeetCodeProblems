class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        
        res[0] = 1
        for i in range(1, length):
            res[i] = nums[i-1] * res[i-1]
            
        postfix = 1
        for i in range(length-1, -1, -1):
            res[i] *= postfix
            postfix *=  nums[i]
        return res