import random

class Game_Controller:
    '''
    Description:
        This class controls all the game behavior
    '''
    def __init__(self):
      self.on_play = True
      self.board = {1:'1',2:'2',3:'3',
                    4:'4',5:'5',6:'6',
                    7:'7',8:'8',9:'9'}
    
    def starter_player(self):
       player = random.randint(1,2)
       if player % 2 == 0:
          return "Player O Starts, select a space:"
       else:
          return "Player X Starts, select a space:"
       
    def print_board(self):
       print(f'{self.board[1]}|{self.board[2]}|{self.board[3]}\n{self.board[4]}|{self.board[5]}|{self.board[6]}\n{self.board[7]}|{self.board[8]}|{self.board[9]}')


if __name__=='__main__':
   controller = Game_Controller()
   controller.starter_player()
   print(controller.starter_player())
   controller.print_board()

    
