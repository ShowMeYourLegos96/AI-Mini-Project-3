def minimax(state):
    # Return the best move for the current player.
    if state.current_player == 1:
        best_value = float('-inf')
        best_move = None
        for move in state.get_legal_moves():
            child = state.make_move(move)
            value = min_value(child)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move
    else:
        # TODO: implement the symmetric case
        # for MIN.
        pass

def max_value(state):
    if state.is_terminal():
        return state.utility()
    v = float('-inf')
    for move in state.get_legal_moves():
        child = state.make_move(move)
        v = max(v, min_value(child))
    return v
    
def min_value(state):
    # TODO: implement. This is symmetric to
    # max_value, but minimizes instead.
    pass


# ADDED ALPHA-BETA PRUNING
def max_value_ab(state, alpha, beta):
    if state.is_terminal():
        return state.utility()
    v = float('-inf')
    for move in state.get_legal_moves():
        child = state.make_move(move)
        v = max(v, min_value_ab(child, alpha, beta))
        if v >= beta:
            return v # Beta cutoff
        alpha = max(alpha, v)
    return v

def min_value_ab(state, alpha, beta):
    # TODO: implement with alpha cutoff.
    pass
