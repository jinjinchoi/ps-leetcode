from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in board:
            row_hash = defaultdict(int)
            for num in row:
                if num is not '.':
                    if row_hash[num] is not 0:
                        return False
                    row_hash[num] += 1
        # check column
        for col_idx in range(len(board)):
            col_hash = defaultdict(int)
            for row_idx in range(len(board)):
                num = board[row_idx][col_idx]
                if num is not '.':
                    if col_hash[num] is not 0:
                        return False
                    col_hash[num] += 1
        # check grid
        for i in range(3):
            for j in range(3):
                grid_hash = defaultdict(int)
                for row in range(3*i, 3*i+3):
                    for col in range(3*j, 3*j+3):
                        num = board[row][col]
                        if num is not '.':
                            if grid_hash[num] is not 0:
                                return False
                            grid_hash[num] += 1
        return True