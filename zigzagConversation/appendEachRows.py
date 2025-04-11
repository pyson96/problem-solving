class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s
        rows = [''] * numRows
        current_row = 0
        going_down = False
        for char in s :
            rows[current_row] += char
            # 0 인덱스와 마지막 인덱스에서 방향 전환
            if current_row == 0 or current_row == numRows - 1 :
                going_down = not going_down
            
            if going_down :
                current_row += 1
            else :
                current_row -= 1
        return ''.join(rows) # string class 의 join 메소드 iterable 객체를 인자로 받아서 문자열을 연결해 줌
    
s = Solution()  
print(s.convert("ABC", 1)) 