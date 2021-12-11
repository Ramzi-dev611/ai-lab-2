from game import Game

initial_stack_size = int(input("Insert the size of the initial stack"))
game = Game(initial_stack_size)
cpu_option = 0
print("Which Bot you want to face ?")
print("1- Slow CPU")
print("2- Fast CPU")
while cpu_option > 2 or cpu_option < 1:
    cpu_option = int(input("Chose an Option : 1 or 2"))

if cpu_option == 1:
    game.start_game()
else:
    pass
