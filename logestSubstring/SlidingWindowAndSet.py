class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        longestLen = 0
        char_set = set()
        while l < len(s) and r < len(s):
            if  s[r] not in char_set or l == r:
                r += 1
                longestLen = max(longestLen , r - l)
            else:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r-1])
        return longestLen
s= Solution()
print(s.lengthOfLongestSubstring("dvdf"))