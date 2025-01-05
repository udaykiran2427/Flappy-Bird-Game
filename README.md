
# Flappy Bird Game

This is a simple implementation of the classic **Flappy Bird** game using **Pygame**. The player controls a bird that must navigate through pipes while avoiding collision with the ground or the pipes. The objective is to survive as long as possible, with the score increasing as the bird passes through pipes.

## Features
- **Gravity & Flap Mechanism**: The bird is affected by gravity, and you can make the bird flap by pressing the spacebar.
- **Pipes Generation**: Pipes are generated randomly and move towards the bird.
- **Collision Detection**: The bird can collide with pipes or the ground, ending the game.
- **Score**: The player gains a point for each pair of pipes successfully passed.
- **Game Over Screen**: A game over screen is displayed when the bird collides with an obstacle.

## Requirements
- Python 3.x
- Pygame library

## Installation

To install Pygame, you can use pip:

```bash
pip install pygame
```

## How to Play
1. Run the game by executing `main.py`.
2. Press **Spacebar** to make the bird flap.
3. Try to avoid colliding with the pipes and the ground.
4. The game ends when the bird collides with an obstacle, and you can restart by pressing **R**.

## Game Controls
- **Spacebar**: Flap the bird
- **R**: Restart the game after a collision

## Assets
The game uses the following images for its assets:
- **assets/bird_down.png**: Bird's downward motion image
- **assets/bird_mid.png**: Bird's mid-flight image
- **assets/bird_up.png**: Bird's upward motion image
- **assets/background.png**: Background image
- **assets/ground.png**: Ground image
- **assets/pipe_top.png**: Top pipe image
- **assets/pipe_bottom.png**: Bottom pipe image
- **assets/game_over.png**: Game over screen image
- **assets/start.png**: Start game screen image

## Code Structure
- **Bird**: A class that controls the bird, including its animation, movement, and collision logic.
- **Pipe**: A class that represents pipes, their movement, and their interaction with the bird.
- **Ground**: A class to handle the movement of the ground.
- **Game loop**: The main game loop which handles input, updates, and rendering of the game.
- **Menu**: A simple menu that shows a start screen and allows the player to begin the game by pressing spacebar.

## License
This project is licensed under the MIT License

## Acknowledgments
- Inspired by the classic Flappy Bird game.
- Pygame for handling game mechanics and rendering.
