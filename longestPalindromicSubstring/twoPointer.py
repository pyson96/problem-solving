class Solution(object):
    originStr : str

    def longestPalindrome(self, s):
        self.originStr = s
        even_str = ""
        odd_str = ""
        answer = ""
        for i, ch in enumerate(s):
            even_str = self.expandPairs(i, i+1,"")
            odd_str = self.expandPairs(i-1,i+1,ch)
            if len(even_str) > len(answer) :
                answer = even_str
            if len(odd_str) > len(answer): 
                answer = odd_str 
        return answer
        
    def expandPairs(self, l, r, s):
        if l < 0 or r >= len(self.originStr) :
            return s
        if self.originStr[l] == self.originStr[r] :
            s = self.originStr[l] + s + self.originStr[r] 
            return self.expandPairs(l-1, r+1 ,s) 
        else : 
            return s
s = Solution()
s.longestPalindrome("a")