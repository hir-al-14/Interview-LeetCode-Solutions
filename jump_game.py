class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(nums):
            # Base Case
            if nums[i] == n:
                return True
            for j in range(0, i, 1):
                a = nums[i]
                if (a + nums[a]) == n:
                    return True
                else:
                    # recursive call