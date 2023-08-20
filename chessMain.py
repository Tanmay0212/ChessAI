import gamestate as gs
from minimax import validActions1


def main():
    state = gs.GameState()
    lst = validActions1(state)

    for i in lst:
        print(i)
        print()

    
    

main()