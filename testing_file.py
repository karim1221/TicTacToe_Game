board = {'1':'1','2':'2','3':'3',
         '4':'4','5':'5','6':'6',
         '7':'7','8':'8','9':'9'}

 
winning_combinations = [[1,2,3],[4,5,6],[7,8,9],
                        [1,4,7],[2,5,8],[3,6,9],
                        [1,5,9],[3,5,7]]

player_spaces = [4,5,6]


for combination in winning_combinations:
    count = 0
    for number in combination:
        if number in player_spaces:
            count += 1
        if count == 3:
            print(combination)
            break