import pygame
from snake import Snake
from pygame.event import Event
from typing import Tuple, Optional


def handle_keys_events(event: Event, selected_index: int) -> Tuple[int, bool]:
    """
    Procesa eventos de teclado para menús (arriba/abajo/enter).

    Args:
        event: evento recibido desde pygame.event.
        selected_index: índice actualmente seleccionado.

    Returns:
        Tuple[selected_index, is_confirm]: índice actualizado y True si se confirmó (Enter).
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            selected_index -= 1
        elif event.key == pygame.K_DOWN:
            selected_index += 1
        elif event.key == pygame.K_RETURN:
            return selected_index, True  

        # loop circular
        selected_index %= 3

    return selected_index, False


def handle_snake_events(event: Event, snake: Snake, move_event: int) -> None:
    """
    Procesa eventos relevantes durante el juego (movimiento periódico y cambios de dirección).

    Args:
        event: evento recibido desde pygame.event.
        snake: instancia de la serpiente a modificar.
        move_event: el identificador del evento de movimiento (pygame.USEREVENT + n).

    Notes:
        - Si event.type == move_event se mueve la serpiente.
        - Si se presiona una flecha se intenta actualizar la dirección.
    """
    if event.type == move_event:
        snake.move_snake()
            
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            snake.update_direction((0, -1))
        elif event.key == pygame.K_DOWN:
            snake.update_direction((0, 1))
        elif event.key == pygame.K_LEFT:
            snake.update_direction((-1, 0))
        elif event.key == pygame.K_RIGHT:
            snake.update_direction((1, 0))
