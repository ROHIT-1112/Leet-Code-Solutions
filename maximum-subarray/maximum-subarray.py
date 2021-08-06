class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cursum = nums[0]
        maxsum = nums[0]
        for n in nums[1:]:
            cursum = max(n, cursum + n)
            maxsum = max(maxsum, cursum)

        return maxsum