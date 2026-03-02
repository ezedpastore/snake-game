import pygame
from constants import COUNTDOWN

def calculate_countdown(countdown_start_time: int) -> int:
    """
    Calcula el número de segundos restantes del countdown basado en el timestamp de inicio.

    Args:
        countdown_start_time: timestamp (ms) en el que empezó el countdown (pygame.time.get_ticks()).

    Returns:
        int: segundos restantes del countdown (puede ser negativo si ya pasó).
    """
    elapsed_time = pygame.time.get_ticks() - countdown_start_time
    seconds_passed = elapsed_time // 1000

    number = COUNTDOWN - seconds_passed

    return number


