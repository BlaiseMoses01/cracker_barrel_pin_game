gi 

# Pin Game Solver

Ths is an algorithm I designed from scratch to find every possible solution to the puzzle game often found at Cracker Barrel restuarants

## Game Rules
### Setup
The game uses a triangular board , typically with 15 holes and 14 pegs

I have defined these using the coordinate system below:
00
10 11
20 21 22
30 31 32 33
40 41 42 43 44

The player can arrange the pegs into the holes in any configuration they please with the empty hole at any position on the board.

Play relies on a pretty basic set of rules, which go as follows: 
### Rules
1) a peg can only be removed from the board by jumping over it with another peg
2) to jump over a peg , there must be an empty hole immediately following the peg being jumped 
3) jumps can be made either diagnoally or horizontally , but must be made in a straight line 

### Win Condition
A player wins when only pin remains on the board 
### Lose Condition
A player loses when no legal moves are possible and more than one pin remains

## Description

I initially started the concept of this program while helping a friend who had chosen to solve the game as a final project. After helping my friend conceptualize the problem , I was intrigued and decided to develop my own solution. 

I chose to use a tree structure paired with a recursive algorithm I designed to exhaustively play every possible move combination for a given board. The algorithm roughly works as follows: 

Once the initial board tree is built , the solve method is started with the head node of the tree, an empty list called trace , which is the moves made in the current search , and an empty list called solutions , which will contain all successful paths that lead to a win 

The algorithm then finds all possible winning combinations using the following recursive structure:

#### Base case 1: Win

In this case, only one pin remains on the board. the trace of moves to reach this state is added to the solutions list, and the function returns

#### Base case 2: Dead end

In this case a losing path has been taken and a dead end is reached, the function can return

#### Recursive case: 

In the recursive case , the board is not in a win state and there are still possible moves. The algorithm finds all of these possible moves, and recursively tests a board with that move made from the current state. 

### Mode 1:
Mode 1 allows the user to custom enter a size and the initial empty hole, essentially creating a custom board that the program will then solve.

### Mode 2: 
Mode 2 is automated to find every legal solution to each possible configuration of the traditional 15 peg board

### Output
The program outputs a text file for each given configuration with the name of the file being the initial empty space on the gameboard. This file will contain the number of solutions, the time it took to solve the board, and a transcript of the move sequences for each legal solution. 

## Getting Started

### Dependencies
* Python, any version should work but I recommend the latest

### Installing

* clone the repo using the command: 
```
git clone https://github.com/BlaiseMoses01/cracker_barrel_pin_game.git
```
Alternatively you can download the repo as a zip from the link in the above command, and extract the files locally.

### Executing program

* Running the Program

* Step 1: Open the cloned repo in a console window or your IDE of choice

* Step 2: Launch the program using the below command 
```
python pingame.py 
```

* Step 3: Choose the mode you wish to use, if you choose option 1 , enter your board size and the starting hole positon.

## Help
Some positions have exponentially more solutions that others, so don't be worried if a solve takes longer than expected. 

## Authors
Blaise Moses (blaisemoses2001@gmail.com)

## License
This project is licensed under the Apache License

## Acknowledgments
I would like to acknowledge my Artificial Intelligence professor Forrest Agostinelli at the Universty  of South Carolina. Though this wasn't for his class his curriculum did peak my interest in search algorithms and game theory style problems. 

