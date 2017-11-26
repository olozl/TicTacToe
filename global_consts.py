X_PLAYER = 'x'
Y_PLAYER = 'o'
EMPTY = '.'
SPACE = ' '
RANDOMNESS_SUFFIX = '#R'
RANDOM_FORMULA = lambda p: (5.0/(p**2))
USAGE = '''Usage: python uttt_game_engine.py <x_player_string> <o_player_string>

You may choose any players from the options below (case sensitive):
  Player String:          Description:
    random          chooses moves randomly
    MM_Cells        Minimax player (with CellsWeightHeu)
    MM_Recursive    Minimax player (with RecursiveWeightHeu)
    MM_Winning      Minimax player (with WinningPossibilitiesHeu) & random jump optimization'''
