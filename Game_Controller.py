import random
import Board_Controller as BC

class Game_Controller:
    '''
    Description:
        This class controls all the game behavior.
    '''
    def __init__(self):
      self.on_play = True
      self.next_turn = 1
      self.player_1: str
      self.player_2: str
      self.board = BC.Board()
    
    def starter_player(self):
       '''
       Definition:
         This method selects randomly which player will start on the first turn.
       '''
       player = random.randint(1,2)
       if player % 2 == 0:
          self.player_1 = 'O'
          self.player_2 = 'X'
          return f"Player O Starts."
       else:
          self.player_1 = 'X'
          self.player_2 = 'O'
          return f"Player X Starts."
       
    def input_validation(self):
       '''
       Definition:
         This method validates that the player Input is a number between 1 and 9.
         if this is a valid entry, it will assign the number to the variable player_input.
       '''

       player_input = input('Please select a space: ')
      
       while player_input not in self.board.board.keys():
         player_input = input('Please select a space from 1 to 9: ')


    def turns_manager(self):
       player_input: int       
       insert_char: str

       if self.next_turn % 2 != 0:
          print(f'Turn {self.next_turn}: Player {self.player_1}')
          insert_char = self.player_1
       else:
          print(f'Turn {self.next_turn}: Player {self.player_2}')
          insert_char = self.player_2

       player_input = self.input_validation()   
       while not self.board.space_validation(player_input, insert_char):
          player_input = self.input_validation()

       self.next_turn +=1


if __name__=='__main__':
   controller = Game_Controller()
   controller.starter_player()
   print(controller.starter_player())
   controller.board.print_board()

    
