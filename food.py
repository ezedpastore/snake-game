import random
from constants import GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from snake import Snake
from typing import Tuple


def generate_food(snake: Snake) -> Tuple[int, int]:
    """
    Genera una posición de comida aleatoria en la grid que no colisione con la serpiente.

    Args:
        snake: instancia Snake, se usa snake.get_body() para evitar generar en el cuerpo.

    Returns:
        (x, y): tupla con coordenadas en celdas (no en pixeles).
    """
    snake_body = snake.get_body()
    
    x = random.randint(1, (SCREEN_WIDTH // GRID_SIZE) - 1)
    y = random.randint(1, (SCREEN_HEIGHT // GRID_SIZE) - 1)
    
    while (x, y) in snake_body:
        x = random.randint(1, (SCREEN_WIDTH // GRID_SIZE) - 1)
        y = random.randint(1, (SCREEN_HEIGHT // GRID_SIZE) - 1)
    
    return (x, y)