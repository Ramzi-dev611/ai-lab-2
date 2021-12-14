# Game of dividing the stacks 
This repository contains the source code for the solution to implement an AI facing the user of this application in a "divide the stacks" game<br>
AI in this game implements to strategies to come up with the best possible move it can make on each turn:
* MINI-MAX game theory algorithm
* ALPHA-BETA pruning 
## Rules of the game 
Starting from a stack with a given size each player should divide an existing stack into two stacks with different sizes <br>
You win the game if you are the last player able to divide an existing stack

## Requirements 
* python 3.x interpreter
* matplotlib library

## Source code 
* **main script** : it starts with asking you to input the initial stack size and choosing which algorithm you want to face than on each turn it asks you to choose a stack and the new stack size
  * **First algorithm** : minmax algorithm named **SLOW CPU**
  * **Second algorithm** : alpha-beta pruning algorithm named **FAST CPU**
  
* **Game script** : This contains a class that contains the methods used to create and maintain a game between the player and a CPU
* **Minmax script** : This is the class that provides the AI logic to implement the minmax and alpha-beta algorithms 

=> By the end of each game a scatter plot is presented showing the number of visited states by the CPU to determine the best move it can make