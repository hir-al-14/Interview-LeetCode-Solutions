class Solution:
    def helper(c, total):
        for j in range(0, c, 1):
            a = nums[j]
            if (a + nums[a]) == total:
                return True
            else:
                if (a + nums[a] + helper(nums[a])) == total:
                    return True
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        out = False
        cur = 0
        if nums[cur] == n:
            return True
        out = helper(nums[cur], n)
        return out