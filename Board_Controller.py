
class Board:
    '''
    Description:
        This class controls the board behavior.
    '''

    def __init__(self):
        self.board = {'1':'1','2':'2','3':'3',
                      '4':'4','5':'5','6':'6',
                      '7':'7','8':'8','9':'9'}
    
    
    def print_board(self):
       '''
        Definition:
            This method prints the board in the terminal.
       '''
       print(f'{self.board['1']}|{self.board['2']}|{self.board['3']}\n{self.board['4']}|{self.board['5']}|{self.board['6']}\n{self.board['7']}|{self.board['8']}|{self.board['9']}')
       
    
    def space_validation(self, space: str, char: str):
        '''
        Definition:
            This method validates if the selected space is available.
        Returns:
            Bool: If the selected space is available the method will return True,
            otherwise it will return false.
        '''
        if space != self.board[space]:
            self.board[space] = char
            return False
        else:
            print(f'The space {space} already contains {self.board[space]}')
            return False
            
            