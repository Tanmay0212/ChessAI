import gamestate as gs
from minimax import validActions


def main():
    state = gs.GameState()
    lst = validActions(state)

    for i in lst:
        print(i)
        print()

main()