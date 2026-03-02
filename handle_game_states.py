import pygame
from game_music import MusicManager
from game_sound import SoundManager
from constants import STATE_MENU, STATE_SETTINGS, STATE_EXIT, STATE_COUNTDOWN
from typing import Tuple


def handle_menu_states(is_option_selected: bool, currently_menu_index: int, state: str, countdown_start_time: int) -> Tuple[str, int]:
    """
    Procesa la selección del menú principal y devuelve el nuevo estado del juego
    junto con el tiempo de inicio del countdown cuando corresponde.

    Args:
        is_option_selected: True si el usuario confirmó una opción (Enter).
        currently_menu_index: índice actualmente seleccionado en el menú.
        state: estado actual del juego.
        countdown_start_time: valor previo del tiempo de inicio del countdown.

    Returns:
        Tuple[state, countdown_start_time]: el nuevo estado y el timestamp del inicio del countdown
        (en ms) si se seleccionó "PLAY", o el countdown_start_time original.
    """
    if is_option_selected:
        if currently_menu_index == 0:
            return STATE_COUNTDOWN, pygame.time.get_ticks()
        elif currently_menu_index == 1:
            return STATE_SETTINGS, countdown_start_time
        else:
            return STATE_EXIT, countdown_start_time

    return state, countdown_start_time


def handle_settings_states(is_setting_selected: bool, currently_settings_index: int, state: str, music: MusicManager, sound: SoundManager) -> str:
    """
    Procesa la selección dentro del menú de ajustes y actualiza estado/recursos.

    Args:
        is_setting_selected: True si el usuario confirmó una opción.
        currently_settings_index: índice seleccionado dentro de ajustes.
        state: estado actual del juego.
        music: instancia de MusicManager para controlar la música.
        sound: instancia de SoundManager para controlar los sonidos.

    Returns:
        state: el estado resultante después de procesar la selección.
    """
    if is_setting_selected:
        if currently_settings_index == 0:
            if music.is_paused:
                music.music_on()
            else:
                music.music_off()
        elif currently_settings_index == 1:
            if sound.is_active:
                sound.sound_off()
            else:
                sound.sound_on()
        else:
            state = STATE_MENU
            
    return state