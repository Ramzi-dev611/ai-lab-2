class MinMax:
    size: int
    state: list
    initial_state: list
    turn: int

    def __init__(self, size: int):
        self.size = size
        self.state = [self.size]
        self.initial_state = [self.size]
        self.turn = 1

    def player(self):
        return self.turn%2 == 0 and "Player" or "CPU"
    def actions(self):
