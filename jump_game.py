class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max distance reachable at start
        max_dist = 0
        n = len(nums)
        # go through each index and update the max duisatnce reachable from start to that index
        for i in range(n):
            # max jump length from that index
            jump_value = nums[i]
            if i > max_dist: # we can't go further than max distance
                return False
            # tracking furthest distance reachable from all positions visited
            max_dist = max(max_dist, i + jump_value)
        # check and return
        if max_dist >= n - 1:
            return True
        else: return False