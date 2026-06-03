class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Create 9 set for each rows, cols, 3x3 square
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for row in range(0,9):
            for col in range(0,9):
                value = board[row][col]
                if value == ".":
                    continue
                #Check row
                if value in rows[row]:
                    return False
                else:
                    rows[row].add(value)
                #Check column
                if value in cols[col]:
                    return False
                else:
                    cols[col].add(value)
                #Check square
                index = (row // 3) * 3 + (col // 3)
                if value in squares[index]:
                    return False
                else:
                    squares[index].add(value)
        return True                