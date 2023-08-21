'''
Nicholas Cali
12/4/2019
I pledge my honor that I have abided by the Stevens Honor System
'''


class Board(object):
    ''' creates the board for the game'''

    def __init__(self, width = 7, height = 6):
        '''constructor for objects of type board'''
        self.width = width
        self.height = height
        self.board = createBoard(width, height)

    def __str__(self):
        '''returns a string representing the board object'''
        x = ""
        for i in self.board:
            for y in i:
                x += '|' + y
            x += "|\n"
        x += '-' * (self.width * 2 + 1)
        x += "\n"
        for w in range(self.width):
            x += " " + str(w)
        return x
        

        

    def allowsMove(self, col):
        '''returns true if board can move into column, returns false if there is no room in column'''
        if col > self.width or col < 0:
            return False

        for r in range(self.height):
            for c in range(self.width):
                if self.board[r][c] == " ":
                    return True

        return False
        
            


    def addMove(self, col, ox):
        '''adds ox variable which holds a string in the column'''
        if self.allowsMove(col):
            for x in range(self.height-1, -1, -1):
                if self.board[x][col] == ' ':
                    self.board[x][col]=ox
                    break



    def setBoard(self, move_string):
        ''' takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'

            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.
            moveString must be a string of integers
        '''
        nextCh = 'X'
        for col_string in move_string:
            col = int(col_string)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'


    def delMove(self, col):
        '''removes the top checker from the col, if empty it does nothing'''
        if col < self.width or col > 0:
            return False
        for i in range(self.height):
            if self.board[i][col] != ' ':
                self.board[i][col] = ' '
                break
                



    def winsFor(self, ox):
        ''' calls game if someone wins by horizontally, diagonally, and vertically'''
        count = 0
        for i in self.board:
            for x in i:
                if x == ox:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
                    
        for col in range(self.width):
            for row in range(self.height):
                if self.board[row][col] == ox:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
            
        count = 0
        for col in range(self.width):
            for row in range(self.height):
                x = col
                y = row
                while x < self.width and y < self.height:
                    if self.board[y][x] == ox:
                        x+=1
                        y+=1
                        count += 1
                    else:
                        break
                        if count == 4:
                            return True

                x = col
                y = row
                while x >= 0 and y < self.height:
                    if self.board[y][x] == ox:
                        x-=1
                        y+=1
                        count += 1
                    else:
                        break
                        if count == 4:
                            return True
                        else:
                            count = 0
        return False
                    




    def hostName(self):
        print('Welcome to Connect 4')
        user = 'X'
        while True:
            c = int(input(user + "'s choice:" ))
            if 0 <= c <= self.width -1:
                self.addMove(c, user)
                print(self)
                if user == "O":
                    user = "X"
                else:
                    user = "O"
            else:
                print('Select a column number')

            if self.winsFor("O"):
                print("Conratulations, O is the winner")
                break
        
            elif self.winsFor("X"):
                print("Congratulations, X is the winner")
                break
                
        
        
        
def createBoard(w, h):
    '''creates a blank board with the given height and width'''
    x = []
    for height in range(h):
        y = []
        for width in range(w):
            y.append(' ')
        x.append(y)
    return x
            
        
        
        

b = Board(6,7)
print(b)
b.hostName()
print(b)    

