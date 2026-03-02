from game_music import MusicManager
from game_sound import SoundManager
from snake import Snake
from constants import GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from draw_game import DrawGame


def check_gameover(snake: Snake) -> bool:
    """
    Comprueba si la serpiente ha chocado con paredes o consigo misma.

    Args:
        snake: instancia Snake.

    Returns:
        True si hay colisión (game over), False en otro caso.
    """
    snake_body = snake.get_body()
    x, y = snake_body[0]

    #collision with walls
    if x < 0 or x >= (SCREEN_WIDTH // GRID_SIZE) or y < 0 or y >= (SCREEN_HEIGHT // GRID_SIZE):	
        return True
    
    #collision with body snake
    if snake_body[0] in snake_body[1:]:
        return True
    
    return False


def handle_gameover(music: MusicManager, sound: SoundManager, draw: DrawGame, snake: Snake) -> bool:
    """
    Ejecuta la secuencia de game over: pausa música, reproduce efecto y dibuja game over.

    Args:
        music: MusicManager para controlar música.
        sound: SoundManager para reproducir efecto.
        draw: DrawGame para dibujar la pantalla de game over.

    Returns:
        was_music_paused: True si se pausó la música (para poder reanudarla después).
    """
    was_music_paused = False
    if not music.is_paused: 
        music.music_off()
        was_music_paused = True
    
    if sound.is_active:
        sound.play_sound()
    
    draw.draw_gameover(snake=snake)
    
    return was_music_paused
