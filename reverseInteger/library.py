class Solution:
    def reverse(self, x: int) -> int:
        positive = x >= 0
        reversed_str = str(x)[::-1] if positive else str(x)[:0:-1] 
        answer = int(reversed_str) * 1 if positive else -int(reversed_str)
        if answer < -2**31 or answer > 2**31 - 1:
            return 0
        return answer

