import Header, Game_Controller as GC

controller = GC.Game_Controller()

while controller.on_play:
    controller.clear_and_print()
    Header.print_tile()
    controller.board.print_board()
    controller.turns_manager()