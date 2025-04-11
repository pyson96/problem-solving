class Solution:
    visitArr : list
    s : str
    answer : str 
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 : return s
        self.visitArr = [False] * len(s)
        self.s = s
        self.answer = ""
        stride = numRows - 1 
        while stride >= 0 :
            i = numRows - stride - 1
            while i < len(self.s):
                i = self.visitNextElement(i)
                i = i + stride * 2       
                if stride == 0 :
                    break
            stride -= 1
        return self.answer
    def visitNextElement(self,idx):
        while idx < len(self.s) :
            self.expandAnswer(idx)
            if idx + 1 < len(self.s) and self.visitArr[idx+1] == True:
                idx += 1
                while idx < len(self.s) and self.visitArr[idx] == True :
                    idx += 1
            else :
                return idx
        return idx
    def expandAnswer(self, idx) :
        self.visitArr[idx] = True
        self.answer = self.answer + self.s[idx]
        
s = Solution()
s.convert("AB",2)
