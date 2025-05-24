import random
import Player as pl
import os
import Board_Controller as BC

class Game_Controller:
    '''
    Description:
        This class controls all the game behavior.
    '''
    def __init__(self):
      self.on_play = True
      self.next_turn = 1
      self.player_1 = pl.Player()
      self.player_2 = pl.Player()
      self.board = BC.Board()
    
    def starter_player(self):
       '''
       Definition:
         This method selects randomly which player will start on the first turn.
       '''
       player = random.randint(1,2)
       if player % 2 == 0:
          self.player_1.char = 'O'
          self.player_2.char = 'X'
          return f"Player O Starts."
       else:
          self.player_1.char = 'X'
          self.player_2.char = 'O'
          return f"Player X Starts."
       
    def input_validation(self, player_char: str):
       '''
       Definition:
         This method validates that the player Input is a number between 1 and 9.
         if this is a valid entry, it will call the method space_validation from Board() class.
       '''

       player_input = input('Please select a space: ')
      
       while player_input not in self.board.board.keys():
         player_input = input('Please select a space from 1 to 9: ')
       
       while self.board.space_validation(player_input, player_char):
          player_input = input('Please select a space: ')


    def game_status(self):
       '''
       Description:
         This method will validated if there still available spaces of it one of the players already won.
       '''
       if self.board.available_spaces == 0:
          print("It's a Tie!!!")
          self.on_play = False

    def turns_manager(self):
       
       if self.next_turn == 1:
          self.starter_player()
       
       if self.next_turn % 2 != 0:
          print(f'Turn {self.next_turn} - {self.board.available_spaces} Available spaces: Player {self.player_1.char}')  
          self.input_validation(self.player_1.char) 

       else:
          print(f'Turn {self.next_turn} - {self.board.available_spaces} Available spaces: Player {self.player_2.char}')
          self.input_validation(self.player_2.char) 
          
      #  self.game_status()
       self.next_turn +=1
    
    def clear_and_print(self):
       '''
         Description:
            This method clears the terminal screen should be called at the and of each turn
       '''
       os.system('cls' if os.name == 'nt' else 'clear')

if __name__=='__main__':
   controller = Game_Controller()
   controller.starter_player()
   print(controller.starter_player())
   controller.board.print_board()

    
