class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dist = 0
        n = len(nums)
        for i in range(nums):
            jump_value = nums[i]
            if i > max_dist:
                return False
            max_dist = max(max_dist, i + jump_value)
        return max_dist