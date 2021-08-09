class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_set = set()
        large_count = 0
        repetation_count = 0
        for i in range(len(s)):
            while s[i] in count_set:
                count_set.remove(s[large_count])
                large_count +=1
            count_set.add(s[i])
            repetation_count = max(repetation_count,i - large_count +1)
        print(repetation_count)
        return repetation_count