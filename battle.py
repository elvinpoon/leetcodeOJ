class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt =  0
        for i in range(len(board)):
            for j in range(len(board[0])):
                flag = 0
                if board[i][j] == 'X':
                    if i == 0 and j ==0:
                        cnt += 1
                        continue
                    if j == 0 and board[i-1][j] != 'X':
                        flag = 1
                    if i == 0 and board[i][j-1] != 'X':
                        flag = 1
                    if i!= 0 and j != 0 and board[i-1][j] != 'X' and board[i][j-1] != 'X':
                        flag = 1
                    if flag:
                        cnt += 1
        return cnt
        