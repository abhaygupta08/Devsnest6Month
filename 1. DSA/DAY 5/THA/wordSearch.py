def chkForWholeWord(i,j,board,leftToChk):
            # print(board)
            if i<0 or i>len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j]!=leftToChk[0]:
                return False

            if len(leftToChk)==1:
                return True
            temp,board[i][j] = board[i][j],' '

            res = chkForWholeWord(i+1,j,board,leftToChk[1:]) or chkForWholeWord(i,j+1,board,leftToChk[1:]) or chkForWholeWord(i-1,j,board,leftToChk[1:]) or chkForWholeWord(i,j-1,board,leftToChk[1:])
            board[i][j] = temp
            return res
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and chkForWholeWord(i,j,board,word):
                    return True
        return False