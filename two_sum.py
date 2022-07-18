class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, current_number in enumerate(nums):
            difference = target - current_number
            if difference in seen:
                return([seen[difference], index])
            else:
                seen[current_number] = index
