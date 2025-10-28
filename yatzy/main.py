from yatzy import *

state = State(sorted(roll_n_dice(5)), 2, frozenset())
while True:
    actions = get_available_actions(state)
    # for i, action in enumerate(actions): print(i, action)
    print(f"State: {state}")
    print("choose action (i) or quit (q)")
    inp = input("> ")
    if inp == "q":
        break

    if inp.isdigit():
        action = Action("reroll", tuple(int(i) for i in inp))
    else:
        action = Action("score", inp)

    assert action in actions

    # idx = int(inp)
    state = transition_func(state, action)
