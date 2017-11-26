import random
import sys
import re
from action import Action

class Agent:
    def choose_act(self, state):
        raise NotImplementedError()

class AlphaBetha(Agent):
    # The searching depth of the alpha-beta. Note that the depth decrease only on opponents turns
    # therefor the actual depth in the game tree is TWICE the value of ALPHA_BETA_DEPTH.
    ALPHA_BETA_DEPTH = 2

    @staticmethod
    def __runAB(eval_func, state):
        acts_res = []
        for act in state.get_legal_actions():
            successor_state = state.generate_successor(act)
            acts_res.append((act, AlphaBetha.__min_val_ab(eval_func, successor_state, AlphaBetha.ALPHA_BETA_DEPTH)))
        _, best_val = max(acts_res, key=lambda x: x[1])
        return random.choice([best_action for best_action, val in acts_res if val == best_val])
    @staticmethod
    def __min_val_ab(eval_func, state, depth, alpha=-sys.maxint, beta=sys.maxint):
        if AlphaBetha.__terminal_test(state, depth):
            return eval_func(state)
        val = sys.maxint
        for act in state.get_legal_actions():
            successor_state = state.generate_successor(act)
            val = min(val, AlphaBetha.__max_val_ab(eval_func, successor_state, depth - 1, alpha, beta))
            if val <= alpha:
                return val
            beta = min(beta, val)
        return val
    @staticmethod
    def __max_val_ab(eval_func, state, depth, alpha=-sys.maxint, beta=sys.maxint):
        if AlphaBetha.__terminal_test(state, depth):
            return eval_func(state)
        val = -sys.maxint
        for act in state.get_legal_actions():
            successor_state = state.generate_successor(act)
            val = max(val, AlphaBetha.__min_val_ab(eval_func, successor_state, depth, alpha, beta))
            if val >= beta:
                return val
            alpha = max(alpha, val)
        return val
    @staticmethod
    def __terminal_test(state, depth):
        return state.is_terminal() or (depth == 0)

    def __init__(self, heuristic, player_obj):
        self._eval_func = heuristic.get_evaluate_function(player_obj)

    def choose_act(self, state):
        return AlphaBetha.__runAB(self._eval_func, state)
class RandomAgent(Agent):
    def choose_act(self, state):
        return random.choice(state.get_legal_actions())

