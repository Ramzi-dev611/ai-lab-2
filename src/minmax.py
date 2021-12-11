class MinMaxPredictor:
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
    def minmax(cls, state: list, turn: bool):
        if cls.final(state):
            return (), cls.utility(state, turn)

        if turn:
            max_evaluation = -1000
            returned_action = ()
            for action in cls.actions(state):
                act, evaluation = cls.minmax(cls.result(state, action), not turn)
                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    returned_action = action
            return returned_action, max_evaluation
        else:
            min_evaluation = 10000
            returned_action = ()
            for action in cls.actions(state):
                taken_action, evaluation = cls.minmax(cls.result(state, action), not turn)
                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    returned_action = action
            return returned_action, min_evaluation

