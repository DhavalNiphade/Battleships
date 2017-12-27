import sys,random
from collections import defaultdict

class Board:
    numBoards = 0
    def __init__(self, size):
        self.size = size
        self.board = self.buildBoard(size)
        Board.numBoards+=1

    def buildBoard(self,size):
        return [[0 for x in range(size)] for y in range(size)]

    def getBoard(self):
        return self.board

    def printBoard(self):
        for row in self.board:
            for col in row:
                print(self.board[row][col])
            print("\n")

    def resetBoard(self):
        self.buildBoard(self.size)

    @classmethod
    def getActiveBoards(cls):
        return cls.numBoards

class Player:

    orient = {'up':(-1,0),'down':(1,0),'left':(0,-1),'right':(0,1)}
    orientationOptions = ['up','down','left','right']

    def __init__(self,numPlayers,name,size):
        self.numPlayers = numPlayers
        self.name = name
        self.score = 0
        self.shipCount = 3
        self.dict = defaultdict()
        self.gameOver = False
        self.myBoard = Board(size)
        self.ShipLoc = set()
        self.nextMove = list()
        self.prevMoves = list()

    @property
    def setMode(self):
        if self.numPlayers > 1:
            self.mode = "Two player"
            return
        self.mode = "AI"
        return

    def placeRandomShips(self):
        ranges = [i for i in range(self.myBoard.size)]
        row = random.choice(ranges)
        col = random.choice(ranges)
        orientation = random.choice(Player.orientationOptions)
        nextRow = row + Player.orient[orientation][0]
        nextCol = row + Player.orient[orientation][1]
        a = 0 <= nextRow < self.myBoard.size
        b = 0 <= nextRow < self.myBoard.size
        if (row,col) in self.ShipLoc or (nextRow,nextCol) in self.ShipLoc or not a or not b:
            self.placeRandomShips()

        self.myBoard.board[row][col] = 1
        self.myBoard.board[nextRow][nextCol] = 1

    # def getCoords(self):
    #     s1 = input("First we enter the 2 square ship. Enter the co-ords for its tail and orientation")
    #     c1,c2,ornt = s1.strip().split()
    #     try:
    #         self.placeShips(c1,c2,ornt,1)
    #     except:
    #         print("Could not place ship, please try again")
    #         self.myBoard.resetBoard()
    #         self.getCoords()
    #
    #     s2 = input("Second we enter the 2 square ship. Enter the co-ords for its tail and orientation")
    #     c1, c2, ornt = s2.strip().split()
    #     try:
    #         self.placeShips(c1, c2, ornt, 1)
    #     except:
    #         print("Could not place ship, please try again")
    #         self.myBoard.resetBoard()
    #         self.getCoords()
    #     self.myBoard.printBoard()
    #
    #     s3 = input("Third we enter the 3 square ship. Enter the co-ords for its tail and orientation")
    #     c1, c2, ornt = s3.strip().split()
    #     try:
    #         self.placeShips(c1, c2, ornt, 1)
    #     except:
    #         print("Could not place ship, please try again")
    #         self.myBoard.resetBoard()
    #         self.getCoords()
    #     self.myBoard.printBoard()

    # def placeShips(self, c1, c2, ornt, ship):
    #     if (self.myBoard.board[c1][c2] != 0):
    #         self.myBoard.board[c1][c2] = ship
    #     else:
    #         return False
    #
    #     nextCoordsX = c1 + self.orient[ornt][0]
    #     nextCoordsY = c2 + self.orient[ornt][1]
    #
    #     if(nextCoordsX > self.size or nextCoordsY > self.size or self.board[nextCoordsX][nextCoordsY]!=0):
    #         print("Cannot place ship there")
    #         return False
    #
    #     self.board[nextCoordsX][nextCoordsY] = ship

    def attack(self):
        if self.nextMove:
            newCoord = self.nextMove.pop()
            if newCoord in self.prevMoves:
                self.attack()
            row = newCoord[0]
            col = newCoord[1]

        # Send the co-ordinates to attack
        else:
            self.newCoord =





class Game(Player):

    def __init__(self,numPlayers,size):
        if size > 1:
            self.Player1 = Player.__init__(numPlayers,"p1",size)
            self.Player2 = Player.__init__(numPlayers,"p2",size)

    def startGame(self,turn):
        self.Player1.getCoords()
        self.Player2.getCoords()
        while(not self.Player1.gameOver or not self.Player2.gameOver):
            if(turn):
                while(self.Player2.attack()):

            else:
                while(self.Player1.attack()):
            turn = (turn+1)%2

def main():
    numPlayers,turn,size = sys.argv[1],sys.argv[2],sys.argv[3]
    game1 = Game(numPlayers,size)
    game1.startGame(turn)

if __name__ == "__main__":
    main()