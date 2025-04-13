import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        left = len(str(x)) // 2 
        right = math.ceil((len(str(x)) / 2 ))
        return str(x)[:left:] == str(x)[-1:right-1:-1]
s = Solution()
s.isPalindrome(1001)