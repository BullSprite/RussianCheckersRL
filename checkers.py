import numpy as np

class Checkers:
    def __init__(self):
        self.board = np.array([[0,-1,0,-1,0,-1,0,-1],
                               [-1,0,-1,0,-1,0,-1,0],
                               [0,-1,0,-1,0,-1,0,-1],
                               [0 for _ in range(8)],
                               [0 for _ in range(8)],
                               [1,0,1,0,1,0,1,0],
                               [0,1,0,1,0,1,0,1],
                               [1,0,1,0,1,0,1,0]])
        self.turn = True

    def __kingCapture(self, x, y, turn):
        ...

    def __capture(self, x, y, turn, isKing):
        legalMoves = []
        if (x == 0 and turn == 1) or (x == 8 and turn == -1):
            isKing = True 
        if isKing: 
            legalMoves += self.__kingCapture(x, y, turn)
        for dir in ((1,1),(1,-1),(-1,1),(-1,-1)):
            deltaX = dir[0]*2 
            deltaY = dir[1]*2
            if -1 < x+deltaX < 8 and -1 < y+deltaY < 8 and self.board[x+dir[0]][y+dir[1]] == turn * -1 and  self.board[x+deltaX][y+deltaY] == 0:
                legalMoves.append((x+deltaX,y+deltaY,turn))
                self.board[x+dir[0]][y+dir[1]] = 0
                self.board[x][y] = 0
                self.board[x+deltaX][y+deltaY] = turn
                legalMoves += self.__capture(x+deltaX, y+deltaY, turn, False)
                self.board[x+dir[0]][y+dir[1]] = turn * -1
                self.board[x][y] = turn
                self.board[x+deltaX][y+deltaY] = 0

        return legalMoves

    def getLegalMoves(self):
        captureMoves = []
        defaultMoves = []
        
        # Directories where piece can move
        if self.turn:
            moveDirectories = [(-1,-1),(-1,1)]
        else:
            moveDirectories = [(1,1),(1,-1)]

        # Current turn number
        turn = 1 if self.turn else -1

        # Search board for current turn pieces and add their possible moves
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != turn and self.board[i][j] != turn * 2:
                    continue
                catures = self.__capture(i, j, turn, self.board[i][j] == 2*turn)
                for cature in catures:
                    captureMoves.append((i, j, *cature))
                if len(captureMoves) != 0:
                    continue

                if self.board[i][j] == turn:
                    if -1 < i+moveDirectories[0][0] < 8 and -1 < j+moveDirectories[0][1] < 8 and self.board[i+moveDirectories[0][0]][j+moveDirectories[0][1]] == 0:
                        defaultMoves.append((i, j, i+moveDirectories[0][0], j+moveDirectories[0][1],
                                           turn * 2 if ((self.turn and i + moveDirectories[0][0] == 0) or (not self.turn and i + moveDirectories[0][0] == 8)) else turn))
                    if -1 < i+moveDirectories[1][0] < 8 and -1 < j+moveDirectories[1][1] < 8 and self.board[i+moveDirectories[1][0]][j+moveDirectories[1][1]] == 0:
                        defaultMoves.append((i, j, i+moveDirectories[1][0], j+moveDirectories[1][1],
                                           turn * 2 if ((self.turn and i+moveDirectories[1][0] == 0) or (not self.turn and i+moveDirectories[1][0] == 8)) else turn))
                        
        if len(captureMoves) > 0: 
            return captureMoves
        return defaultMoves
                    
            
                    
