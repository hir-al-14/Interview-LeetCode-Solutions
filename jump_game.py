class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dist = 0
        n = len(nums)
        for i in range(n):
            jump_value = nums[i]
            if i > max_dist:
                return False
            max_dist = max(max_dist, i + jump_value)
        if max_dist == n:
            return True
        else: return False