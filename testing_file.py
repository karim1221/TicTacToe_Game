board = {'1':'1','2':'2','3':'3',
         '4':'4','5':'5','6':'6',
         '7':'7','8':'8','9':'9'}

selection = input('number: ')

if selection not in board.keys():
    print(selection)
# while selection != 'a':
#     selection = input('number: ')
#     print(board[selection])d