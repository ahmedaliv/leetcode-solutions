class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ps = copy.deepcopy(matrix)
        self.pre_row()

    def pre_row(self):
        rows = len(self.ps)
        cols = len(self.ps[0])
        for r in range(rows):
            for c in range(1,cols):
                self.ps[r][c]+=self.ps[r][c-1]
    # def pre_col():
    #     rows = len(self.ps)
    #     cols = len(self.ps)
    #     for c in range(cols):
    #         for r
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1,row2+1):
            if col1:
                total+=self.ps[r][col2]-self.ps[r][col1-1]
            else:
                total+=self.ps[r][col2]

        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)