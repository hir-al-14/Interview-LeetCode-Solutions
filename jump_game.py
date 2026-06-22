class Solution:
    def helper(c, total):
        for j in range(0, c, 1):
            a = nums[c]
            if (a + nums[a]) == total:
                return True
            else:
                if (a + nums[a] + helper(nums[a])) == total:
                    return True
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        out = False
        for i in range(nums):
            # Base Case
            if nums[i] == n:
                return True
            out = helper(i, n)
        return out