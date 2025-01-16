class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ps = copy.deepcopy(matrix)
        self.pre_row()
        self.pre_col()

    def pre_row(self):
        rows = len(self.ps)
        cols = len(self.ps[0])
        for r in range(rows):
            for c in range(1,cols):
                self.ps[r][c]+=self.ps[r][c-1]
    def pre_col(self):
        rows = len(self.ps)
        cols = len(self.ps[0])
        for c in range(cols):
            for r in range(1,rows):
                self.ps[r][c] += self.ps[r-1][c]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.ps[row2][col2]
        total-=self.ps[row1-1][col2] if row1 >0 else 0
        total-=self.ps[row2][col1-1]if col1>0 else 0
        total+=self.ps[row1-1][col1-1] if row1>0  and col1 > 0 else 0
        return total



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)