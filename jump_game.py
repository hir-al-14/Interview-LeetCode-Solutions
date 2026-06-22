class Solution:
    def helper(self, nums, c, total):
        if c >= total:
            return True
        for j in range(0, nums[c], 1):
            a = nums[j]
            if self.helper(nums, c + j, total):
                return True
        return False
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        out = False
        cur = 0
        out = self.helper(nums, cur, n-1)
        return out