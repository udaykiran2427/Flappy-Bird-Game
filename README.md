# Flappy Bird Game

A simple **Flappy Bird** game implemented with **Pygame**, where the player controls a bird to navigate through pipes, avoiding collisions. The goal is to survive and score by passing pipes.

## Features
- **Gravity & Flap**: Press spacebar to make the bird flap.
- **Pipes Generation**: Randomly moving pipes.
- **Collision Detection**: Collide with pipes or ground to end the game.
- **Score**: Points increase by passing pipes.
- **Game Over**: Displayed after a collision.

## Requirements
- Python 3.x
- Pygame

## Installation
```bash
pip install pygame
```

## How to Play
1. Run `main.py`.
2. Press **Spacebar** to flap.
3. Avoid pipes and the ground.
4. Restart with **R** after a collision.

## Controls
- **Spacebar**: Flap
- **R**: Restart

## Assets
- Bird, pipes, background, ground, game over, and start images.

## Code Structure
- **Bird**: Controls bird movement and collisions.
- **Pipe**: Handles pipes and interactions.
- **Ground**: Manages ground movement.
- **Game loop**: Main game logic.
- **Menu**: Start screen.

## Acknowledgments
- Inspired by Flappy Bird.
- Built with Pygame.
