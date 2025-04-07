class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        longestLen = 0
        charSet = set()
        while l < len(s) and r < len(s):
            if  s[r] not in charSet or l == r:
                r += 1
                longestLen = max(longestLen , r - l)
            else:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r-1])
        return longestLen
s= Solution()
print(s.lengthOfLongestSubstring("dvdf"))