import numpy as np
import random


array=np.array
zeros = np.zeros

go_board = array([["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9])
#print(go_board)

n=1
while n < 50:
    # black turn plays 1
    black = True
    while black == True:
        r,c = random.randint(1,9)-1,random.randint(1,9)-1
        if go_board[r][c] == '.':
            go_board[r][c] = 'X'
            black = False
            n+=1
            break

    while black != True:
        r,c = random.randint(1,9)-1,random.randint(1,9)-1
        if go_board[r][c] == '.':
            go_board[r][c] = 'O'
            black = True
            n+=1
            break
    
#print(go_board)

rowmax, colmax = 9,9

class Position:    
    def __init__(self,r,c):
        self.color = '.'
        self.r = r-1
        self.c = c-1
        self.up, self.down, self.left, self.right = 1,1,1,1
        if r == 1: self.up = 0
        if c == 1 : self.left = 0
        if r == rowmax: self.down = 0
        if c == colmax: self.right = 0
        self.liberties = self.up + self.down + self.right + self.left

    
    def __repr__(self):
        if self.color=='.': return '. ' #'.'+str(self.liberties)
        return self.color+str(self.liberties) #+str(self.up)+str(self.right)+str(self.down)+str(self.left)+' '+str(self.liberties)
    
    def get_neighbors(self):
        self.neighbors=[]
        if self.r-1>=0 :
            self.neighbors.append(grid[self.r-1][self.c].color)
        if self.r+1<9 :
            self.neighbors.append(grid[self.r+1][self.c].color)
        if self.c-1>=0 :
            self.neighbors.append(grid[self.r][self.c-1].color)
        if self.c+1<9 :
            self.neighbors.append(grid[self.r][self.c+1].color)        
    
    def update_liberties(self):
        self.liberties = self.up + self.down + self.right + self.left
    
    def update_position(self, color):
        self.update_liberties()
        self.get_neighbors()
        if self.liberties==1 and (self.color not in self.neighbors) and (self.color != color):
            self.color='.'
            if self.r-1>=0 :
                grid[self.r-1][self.c].down+=1;
                grid[self.r-1][self.c].update_liberties() 
                if grid[self.r-1][self.c].color=='.' :
                    self.up+=1
                   
            if self.r+1<9 :
                grid[self.r+1][self.c].up+=1;
                grid[self.r+1][self.c].update_liberties()
                if  grid[self.r+1][self.c].color=='.':
                    self.down+=1
                
            if self.c-1>=0 :
                grid[self.r][self.c-1].right+=1;
                grid[self.r][self.c-1].update_liberties()
                if grid[self.r][self.c-1].color=='.':
                    self.left+=1
                
            if self.c+1<9 :
                grid[self.r][self.c+1].left+=1;
                grid[self.r][self.c+1].update_liberties()
                if grid[self.r][self.c+1].color=='.':
                    self.right+=1
                
        self.update_liberties()
            
    def reset_up(self, color):
        self.up = 0
        #self.update_liberties()
        self.update_position(color)
        
    def reset_down(self, color):
        self.down = 0
        #self.update_liberties()
        self.update_position(color)
        
    def reset_left(self, color):
        self.left = 0
        #self.update_liberties()
        self.update_position(color)
        
    def reset_right(self, color):
        self.right = 0
        #self.update_liberties()
        self.update_position(color)
    
    def play(self,color):
        error = False
        if self.color=='.':
            self.color = color
        else:
            error=True
            print('*************** Error : Position not empty')
            return error
        
        if self.r-1>=0 :
            if grid[self.r-1][self.c].color!='.':
                self.reset_up(self.color)
            grid[self.r-1][self.c].reset_down(self.color)
               
        if self.r+1<9 :
            if grid[self.r+1][self.c].color!='.':
                 self.reset_down(self.color)
            grid[self.r+1][self.c].reset_up(self.color)
        if self.c-1>=0 :
            if grid[self.r][self.c-1].color!='.':
                 self.reset_left(self.color)
            grid[self.r][self.c-1].reset_right(self.color)
        if self.c+1<9 :
            if grid[self.r][self.c+1].color!='.':
                self.reset_right(self.color);
            grid[self.r][self.c+1].reset_left(self.color)
        # position played
        #self.update_position(self.color)
        return error
        

def test_class():        
    pos1 = Position(1,1)
    print(pos1)

    pos2 = Position(2,5)
    print(pos2)

    pos3 = Position(3,9)
    print(pos3)


def grid_state():
    black_score, black_stones = 0, 0
    white_score, white_stones = 0, 0
    for r in range(0,rowmax):
        for c in range(0,colmax):
            if grid[r][c].color!='.':
                if grid[r][c].color == 'B':
                    black_stones += 1
                    black_score += grid[r][c].liberties 
                else:
                    white_stones += 1
                    white_score += grid[r][c].liberties
    return "".join(('B: ',str(black_stones),'/', str(black_score), '  W:', str(white_stones),'/', str(white_score)))
                    
    
grid = np.ndarray((9,9), dtype=Position)
for r in range(1,10):
    for c in range(1, 10):
        grid[r-1][c-1] = Position(r,c)

# some first moves
# black play
grid[1][1].play('B')
# white play
grid[1][2].play('W')

# black play
grid[0][1].play('B')
# white play
grid[1][8].play('W')

# black play
grid[1][7].play('B')
# white play
grid[2][7].play('W')

print(grid, grid_state())
# black play
grid[2][2].play('B')
# white play
grid[2][6].play('W')

print(grid, grid_state())

def game():
    player='B'
    while True:
        print(player, 'plays ! Enter r,c : ',end='')
        r, c = input().split(',')
        error = grid[int(r)-1][int(c)-1].play(player)
        if player=='B' and not error: player='W'
        else:
            if player=='W' and not error: player='B'
        print(grid)
        print('Score (stones/liberties) : ',grid_state())

game()