import Header, Game_Controller as GC


controller = GC.Game_Controller()

Header.print_tile()
print(controller.starter_player())

while controller.on_play:
    controller.board.print_board()
    controller.turns_manager()