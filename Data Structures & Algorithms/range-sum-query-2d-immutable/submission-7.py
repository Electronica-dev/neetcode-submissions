class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows = len(matrix)
        cols = len(matrix[0])
        self.sums = matrix

        for i in range(rows):
            for j in range(cols):
                if j - 1 < 0:
                    continue
                self.sums[i][j] += self.sums[i][j - 1]
        
        for j in range(cols):
            for i in range(rows):
                if i - 1 < 0:
                    continue
                self.sums[i][j] += self.sums[i - 1][j]
        



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows = row2 - row1 + 1
        cols = col2 - col1 + 1
        
        i_1, j_1 = row2 - rows, col2
        i_2, j_2 = row2, col2 - cols
        res = 0
        
        print(i_1, i_2, j_1, j_2)
        curr_sum = self.sums[row2][col2]
        if i_1 < 0 or j_2 < 0:
            if i_1 < 0 and j_2 < 0:
                return curr_sum
            elif i_1 < 0:
                return curr_sum - self.sums[i_2][j_2]
            elif j_2 < 0:
                return curr_sum - self.sums[i_1][j_1]
        print(curr_sum)
        print(self.sums[i_1][j_1])
        print(self.sums[i_2][j_2])
        return curr_sum - self.sums[i_1][j_1] - self.sums[i_2][j_2] + self.sums[row1 - 1][col1 - 1]

        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)