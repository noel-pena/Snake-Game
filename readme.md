# Python Snake Game

This is a simple Snake game implemented in Python using the Pygame library.

## Features

- Classic Snake game mechanics
- Score tracking
- Increasing speed as score increases

## Dependencies

- Python 3.x
- Pygame library

## Getting Started

To run the game locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/noel-pena/Snake-Game.git
```

2. Install dependencies:

```bash
pip3 install pygame
```

3. Start the game:

```bash
python3 main.py
```

5. Use the arrow keys to control the snake's movement.

- UP arrow key: Move the snake up
- DOWN arrow key: Move the snake down
- LEFT arrow key: Move the snake left
- RIGHT arrow key: Move the snake right
- ESCAPE key: Exits game

6. Avoid running into walls or the snake's own body.
7. Collect fruits to increase your score.

## Structure

The project structure is organized as follows:

- `main.py`: Main Python script containing the game logic.
- `fruit.py`: Class for the fruit object.
- `snake.py`: Class for the snake object.
- `pics/`: Directory containing images.
- `sound/`: Directory containing the crunch sound.
