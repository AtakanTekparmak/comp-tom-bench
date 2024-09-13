# LLM-COMP-TOM

## Introduction

The competitive game for this experiment is a **Mod Game (N=16) with Public Betting**.

### Game Overview
- The game consists of 16 players and 16 possible numbers/actions (0 to 16).
- The game is played for 100 turns.

### Game Rules
1. Each turn:
   - Each player publicly bets on the number they think will come up the most.
   - Each player then privately chooses a number/action.
   - After private votes are revealed, players receive points based on the scoring rubric.

2. The game ends after 100 turns.

### Scoring Rubric
- Players receive one point per other player that chose their selected number/action minus one.
- Players receive 0.5 points per player that chose the number they bet on.

## Requirements
- Python 3.10+
- pip

## Setup
1. Set up a virtual environment and install dependencies:
```
make install
```

## Running the Game
```
make run
```
