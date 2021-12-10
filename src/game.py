class Game:
    size: int
    state: list
    actions = {}

    def __init__(self, size):
        self.size = size
        self.state = [size]

    def game_over(self):
        over = True
        for stackSize in self.state:
            if stackSize > 2:
                over = False
                break
        return over

    def change_stack(self, index, old, new):
        self.state = [*self.state[:index], old-new, new, *self.state[index+1:]]
        self.state.sort()

    def player_move(self):
        if self.game_over():
            print("Game over. You lost")
        else:
            if len(self.state) > 1:
                stack_index = 0
                while stack_index == 0 or stack_index > len(self.state) or self.state[stack_index] <= 2:
                    stack_index = int(input("Which stack you want to divide next? ")) - 1
                stack_to_be_changed = self.state[stack_index]
                stack_size = 0
                while stack_size == 0 or stack_size > stack_to_be_changed - 1 or stack_to_be_changed == 2*stack_size:
                    stack_size = int(input("Give a valid size of the new stack"))
                self.change_stack(stack_index, stack_to_be_changed,stack_size)
            else:
                stack_size = 0
                while stack_size == 0 or stack_size > self.state[0] - 1 or self.state[0] == stack_size * 2:
                    stack_size = int(input("Give a valid size of the new stack"))
                self.change_stack(0, self.state[0], stack_size)

    def cpu_find_best_move(self):
        pass

    def cpu_move(self):
        if self.game_over():
            print("Good Game, you won")
        else:
            index, size = self.cpu_find_best_move()
            self.change_stack(index, self.state[index], size)