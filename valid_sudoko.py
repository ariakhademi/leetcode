"""
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must 
contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

        # check rows
        seen = []
        for row in board:
            for i in range(len(board)):
                print(seen)
                if row[i] != '.':
                    if row[i] in seen:
                        return False
                    else:
                        seen.append(row[i])
            seen = []
        
        # check columns
        seen = []
        for i in range(len(board[0])):
            for row in board:
                if row[i] != '.':
                    if row[i] in seen:
                        return False
                    else:
                        seen.append(row[i])
            seen = []

        # check each sub-box
        seen = []
        for divider in [0,3,6]:
            for j in range(divider, divider + 2):
                for row in board[divider: divider + 2]:
                    if row[j] != '.':
                        if row[j] in seen:
                            return False
                        else:
                            seen.append(row[j])
                seen = []
        
        return True