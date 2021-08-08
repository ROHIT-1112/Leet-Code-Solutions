class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        current_sum =0
        for i in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum +=i
            maxsum = max(maxsum,current_sum)
        return maxsum