class Solution:
    def myAtoi(self, s: str) -> int:
        is_negative = 1
        s = s.strip()
        if s == "" : return 0
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-' : is_negative = -1
            s = s[1::]
        answer = 0
        for ch in s :
            num = ord(ch) - ord('0')
            if num < 0 or num > 9 :
                break
            answer *= 10
            answer += num
        answer *= is_negative 
        if answer < -2**31 :
            answer = -2**31
        if answer > 2**31 - 1 :
            answer = 2**31 - 1
        return answer

