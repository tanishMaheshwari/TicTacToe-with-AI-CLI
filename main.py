# Project By Tanish Maheshwari


class gameEngine:
    def __init__(self) -> None:
        # import numpy as 
        from numpy import array
        self.board = array([0 for i in range(9)])
        self.board = self.board.reshape(3, 3)
        self.moveOfPlayer = 1
        self.moveCounter = 0
        # 0 - Empty Space
        # 1 - Player 1's marker
        # 2 - Player 2's Marker

    def bestMove(self):
        self.boardList = self.board.tolist()
        if self.checkWin() != 0:
            return None
        # Check For Win
        if self.moveOfPlayer == 1:
            a = [1, 2]
        else:
            a = [2, 1]
        for k in a:
            for i in range(3): # Check for horizontal win
                if self.boardList[i] in [[0, k, k], [k, 0, k], [k, k, 0]]:
                    return [i, self.boardList[i].index(0)]

            for i in range(3): # Check for vertical win
                for i in range(3):
                    self.vs = [self.boardList[0][i], self.boardList[1][i], self.boardList[2][i]] # Vertical Strips
                    if self.vs in [[0, k, k], [k, 0, k], [k, k, 0]]:
                        return [self.vs.index(0), i]
            # Check for Diagonal win
            if [self.boardList[0][0],self.boardList[1][1], self.boardList[2][2]] in [[0, k, k], [k, 0, k], [k, k, 0]]:
                return [[self.boardList[0][0],self.boardList[1][1], self.boardList[2][2]].index(0) for i in range(2)]
            if [self.boardList[0][2-0],self.boardList[1][2-1], self.boardList[2][2-2]] in [[0, k, k], [k, 0, k], [k, k, 0]]:
                return [[self.boardList[0][2],self.boardList[1][1], self.boardList[2][0]].index(0), 2-[self.boardList[0][2],self.boardList[1][1], self.boardList[2][0]].index(0)]
        # If no Win
        # If center free
        if self.boardList[1][1] == 0:
            return [1, 1]
        # If diagonals free
        if self.boardList[0][0] == 0:
            return [0, 0]
        if self.boardList[0][2] == 0:
            return[0, 2]
        if self.boardList[2][0] == 0:
            return [2, 0]
        if self.boardList[2][2] == 0:
            return [2, 2]
        
        # just make a possible move

        for i in range(3):
            for j in range(3):
                if self.boardList[i][j] == 0:
                    return [i, j]
        # END
        
    def checkIfLegal(self, move):
        if self.board[move[0], move[1]] == 0:
            return True
        else:
            return False
    def checkWin(self):
        self.boardList = self.board.tolist()
        for k in range(1, 3):
            for i in range(3):
                if self.boardList[i] == [k, k, k]:
                    return k
                if [self.boardList[0][i], self.boardList[1][i], self.boardList[2][i]] == [k, k, k]:
                    return k
            if [self.boardList[0][0],self.boardList[1][1], self.boardList[2][2]] == [k, k, k]:
                return k
            if [self.boardList[0][2-0],self.boardList[1][2-1], self.boardList[2][2-2]] == [k, k, k]:
                return k
        for i in range(3):
            for j in range(3):
                if self.boardList[i][j] == 0:
                    return 0
        return 3        
    
    def printBoard(self):
        for i in range(len(self.board)):
            j = self.board[i].tolist()
            print('X', end='') if j[0] == 1 else  print('O', end='') if j[0] == 2 else print(' ', end='')
            print(' | ', end='')
            print('X', end='') if j[1] == 1 else  print('O', end='') if j[1] == 2 else print(' ', end='')
            print(' | ', end='')
            print('X', end='') if j[2] == 1 else  print('O', end='') if j[2] == 2 else print(' ', end='')
            print('\n--+---+--') if i != 2 else print()
    def makeMove(self, m):
        if self.checkIfLegal(m):
            self.moveCounter +=1
            self.board[m[0]][m[1]] = self.moveOfPlayer
            # print(m)
            if self.moveOfPlayer == 1:
                self.moveOfPlayer = 2 
            else:
                 self.moveOfPlayer = 1
            return 0
        else:
            return 1
        pass

if __name__=="__main__":
    engine = gameEngine()
    print("Tic Tac Toe By Tanish Maheshwari")
    engine.printBoard()
    print()
    whichPlayer = int(input("Which Player do you want to be (1/2): "))
    print("Enter your move in the format row <space> column")
    if whichPlayer == 2:
        engine.makeMove(engine.bestMove())
    while True:
        engine.printBoard()
        if engine.makeMove([int(i) - 1 for i in input('-> ').split()]) == 1:
            print("Illegal move. Please Try Again")
            continue
        else:
            if engine.checkWin() in [1, 2]:
                print("Player", engine.checkWin(), "wins!")
                print("You were Player", whichPlayer)
                break
            if engine.checkWin() == 3:
                print("Tie")
                break

            engine.makeMove(engine.bestMove())
            if engine.checkWin() in [1, 2]:
                print()
                engine.printBoard()
                print("Player", engine.checkWin(), "wins!")
                print("You were Player", whichPlayer)
                break
            if engine.checkWin() == 3:
                print()
                engine.printBoard()
                print("Tie")
                break
            print()