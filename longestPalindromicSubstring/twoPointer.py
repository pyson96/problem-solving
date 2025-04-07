class Solution(object):
    originStr : str

    def longestPalindrome(self, s):
        self.originStr = s
        evenStr = ""
        oddStr = ""
        answer = ""
        for i, ch in enumerate(s):
            evenStr = self.expandPairs(i, i+1,"")
            oddStr = self.expandPairs(i-1,i+1,ch)
            if len(evenStr) > len(answer) :
                answer = evenStr
            if len(oddStr) > len(answer): 
                answer = oddStr 
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