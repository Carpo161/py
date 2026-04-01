from random import randint
class Game():

    def __init__(self):
        self.display = []
    
    def create_display(self):
        for i in range(4):
            row = []
            for j in range(4):
                row.append(f'{'0':^5}')
            self.display.append(row)
        return self.display
    
    def show_display(self):
        for row in self.display:
            for i in row:
                print(i, end='')
            print()
    
    def change_display(self,row,col,val):
        self.display[row][col] = f'{val:^5}'
        return self.display
    
    def player_input(self):
        direc = input('Use the arrow keys to move...')
        while direc not in ['w','a','s','d']:
            print('Invalid input')
            direc = input('Use the arrow keys to move...')
        return direc
    
    def merge(self, direc):
        if direc == 'w':
            for i,row in enumerate(self.display):
                if i == 0:
                    continue
                for index,item in enumerate(row):
                    if item != '0':
                        self.display[i-1].insert(index,self.display[i].pop(index))
                        self.display[i].insert(index,f'{'0':^5}')


g = Game()
g.create_display()
g.change_display(0,1,'2048')
g.change_display(1,2,'2048')
g.change_display(2,3,'2048')
g.change_display(3,0,'2048')
g.show_display()
g.merge(g.player_input())
g.show_display()

'''
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 2, 0]
'''