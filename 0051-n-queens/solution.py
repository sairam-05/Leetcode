class Solution:

    def display(self,board,result):
        ans_list=[]
        for i in board:
            ans=''.join(i)
            ans_list.append(ans)
        result.append(ans_list)
    def backtrack(self,row , colSet , posDiagonal , negDiagonal , board,n,result):
        #base condition
        if row == n:
            self.display(board,result)
            return
        
        for col in range(0,n):
            neg = row - col
            pos = row + col
            if col not in colSet and pos not in posDiagonal and neg not in negDiagonal:
                colSet.add(col)
                posDiagonal.add(pos)
                negDiagonal.add(neg)
                board[row][col] = "Q"
                self.backtrack(row + 1 ,colSet , posDiagonal , negDiagonal , board,n,result)
                colSet.remove(col)
                posDiagonal.remove(pos)
                negDiagonal.remove(neg)
                board[row][col] = "."



    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        result=[]
        self.backtrack(0, set() , set() , set() , board,n,result)
        return result
