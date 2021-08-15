class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nset = set(nums)
        if len(nset) < len(nums):
            return True
        return False
        