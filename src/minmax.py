class MinMaxPredictor:
    visited_states = {}

    @classmethod
    def actions(cls, state: list):
        output = []
        for index, stack in enumerate(state):
            if stack <= 2:
                continue
            else:
                for newSize in range(1, int(stack / 2) + 1):
                    if newSize * 2 == stack:
                        continue
                    output.append((index, newSize))
        return output

    @classmethod
    def result(cls, state: list, action: tuple):
        index, new_size = action
        old = state[index]
        state = [*state[:index], old - new_size, new_size, *state[index + 1:]]
        state.sort()
        return state

    @classmethod
    def final(cls, state: list):
        game_state = True
        for stack in state:
            if stack > 2:
                game_state = False
                break
        return game_state

    @classmethod
    def utility(cls, state: list, turn: bool):
        if cls.final(state):
            if turn:
                return -1
            else:
                return 1

    @classmethod
    def minmax(cls, state: list, turn: bool, number_visited_states: int = 0):
        if cls.final(state):
            return (), cls.utility(state, turn), number_visited_states + 1

        key = " "
        key = turn and key.join([str(num) for num in state])+" : 1" or key.join([str(num) for num in state])+" : -1"
        if key in cls.visited_states:
            return (), cls.visited_states[key], number_visited_states+1

        if turn:
            max_evaluation = -1000
            returned_action = ()
            returned_number = 0
            for action in cls.actions(state):
                _, evaluation, number = cls.minmax(cls.result(state, action), not turn, number_visited_states)
                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    returned_action = action
                returned_number += number
            cls.visited_states[" ".join([str(num) for num in state])+" : 1"] = max_evaluation
            return returned_action, max_evaluation, returned_number+1
        else:
            min_evaluation = 10000
            returned_action = ()
            returned_number = 0
            for action in cls.actions(state):
                _, evaluation, number = cls.minmax(cls.result(state, action), not turn, number_visited_states)
                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    returned_action = action
                returned_number += number
            cls.visited_states[" ".join([str(num) for num in state]) + " : -1"] = min_evaluation
            return returned_action, min_evaluation, returned_number+1

    @classmethod
    def alpha_beta(cls, state: list, turn: bool, alpha: int = 10000, beta: int = -10000, number_visited_states: int = 0):
        if cls.final(state):
            return (), cls.utility(state, turn), number_visited_states + 1
        key = " "
        key = turn and key.join([str(num) for num in state]) + " : 1" or key.join([str(num) for num in state]) + " : -1"
        if key in cls.visited_states:
            return (), cls.visited_states[key], number_visited_states + 1

        if turn:
            max_evaluation = -1000
            returned_action = ()
            returned_number = 0
            for action in cls.actions(state):
                _, evaluation, number = cls.alpha_beta(cls.result(state, action), not turn, alpha, beta, number_visited_states)
                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    returned_action = action
                returned_number += number
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            cls.visited_states[" ".join([str(num) for num in state]) + " : 1"] = max_evaluation
            return returned_action, max_evaluation, returned_number + 1
        else:
            min_evaluation = 10000
            returned_action = ()
            returned_number = 0
            for action in cls.actions(state):
                _, evaluation, number = cls.alpha_beta(cls.result(state, action), not turn, alpha, beta, number_visited_states)
                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    returned_action = action
                returned_number += number
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            cls.visited_states[" ".join([str(num) for num in state]) + " : -1"] = min_evaluation
            return returned_action, min_evaluation, returned_number + 1


