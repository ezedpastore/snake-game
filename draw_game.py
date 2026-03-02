import pygame
from pygame import Surface
from constants import WHITE, LIGHT_GREEN, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, COUNTDOWN, GRID_SIZE
from countdown import calculate_countdown
from game_music import MusicManager
from game_sound import SoundManager
from image_uploader import load_image
from snake import Snake
from typing import Tuple


class DrawGame:
    """
    Clase responsable de todo el renderizado: menú, ajustes, juego, countdown y gameover.
    Mantiene las fuentes y fondos ya cargados para que las funciones de dibujo sean ligeras.
    """
    screen: Surface
    title_font: pygame.font.Font
    menu_font: pygame.font.Font
    settings_font: pygame.font.Font
    gameover_font: pygame.font.Font
    score_font: pygame.font.Font
    score_msg_font: pygame.font.Font
    countdown_font: pygame.font.Font
    ingame_background: Surface
    menu_background: Surface
    
    def __init__(self, screen: Surface) -> None:
        """
        Inicializa fuentes y carga imágenes de fondo.

        Args:
            screen: Surface principal donde se dibuja el juego.
        """
        self.screen = screen
        
        # setting up fonts
        self.title_font = pygame.font.SysFont("candara", 110, bold=True)
        self.menu_font = pygame.font.SysFont("candara", 45)
        self.settings_font = pygame.font.SysFont("candara", 45)
        self.gameover_font = pygame.font.SysFont("candara", 60)
        self.score_font = pygame.font.SysFont("candara", 40)
        self.score_msg_font = pygame.font.SysFont("candara", 25)
        self.countdown_font = pygame.font.SysFont("candara", 60)
        
        # loading snake game images
        self.ingame_background = load_image("assets/images/snake_background.png")
        self.menu_background = load_image("assets/images/menu_background.png")
        

    def draw_countdown(self, countdown_start_time: int) -> bool:
        """
        Dibuja el countdown en pantalla usando el tiempo de inicio.
        No llama a pygame.display.update(); sólo blitea en el Surface.

        Args:
            countdown_start_time: timestamp (ms) del inicio del countdown.

        Returns:
            True si el countdown ya finalizó (tiempo total excedido), False en otro caso.
        """
        self.screen.blit(self.ingame_background, (0, 0))

        number = calculate_countdown(countdown_start_time)

        if number > 0:
            text = self.countdown_font.render(str(number), True, WHITE)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            
            self.screen.blit(text, rect)
        else:
            text = self.countdown_font.render("Go!", True, WHITE)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            
            self.screen.blit(text, rect)
            
        if (pygame.time.get_ticks() - countdown_start_time) // 1000 >= (COUNTDOWN + 1):
            return True
        
        return False


    def draw_food(self, position: Tuple[int, int]) -> None:
        """
        Dibuja la comida en la posición de la cuadrícula.

        Args:
            position: (x, y) en celdas de GRID_SIZE.
        """
        rect = pygame.Rect(
            (position[0] * GRID_SIZE), 
            (position[1] * GRID_SIZE), 
            GRID_SIZE, 
            GRID_SIZE
        )
        
        pygame.draw.rect(self.screen, "red", rect)


    def draw_gameover(self, snake: Snake) -> None:
        """
        Dibuja la pantalla de 'GAME OVER'. No hace update de pantalla.
        """
        game_over = self.gameover_font.render("GAME OVER", True, WHITE)
        self.screen.fill(BLACK)
        self.screen.blit(game_over, (200, 220))
        
        #centering the score message horizontally 
        score_msg = self.score_msg_font.render(f"YOUR SCORE WAS {snake.get_score()}", True, WHITE)
        self.screen.blit(score_msg, score_msg.get_rect(center=(self.screen.get_width() // 2, 350)))
        
        
    def draw_menu(self, selected_index: int) -> None:
        """
        Dibuja el menú principal con la opción seleccionada resaltada.

        Args:
            selected_index: índice de la opción del menú a resaltar.
        """
        self.screen.blit(self.menu_background, (0, 0))

        #darkens the screen
        self.draw_overlay()

        #centering the title horizontally 
        title = self.title_font.render("SNAKE GAME", True, WHITE)
        self.screen.blit(title, title.get_rect(center=(self.screen.get_width() // 2, 100)))

        options = ["PLAY", "SETTINGS", "EXIT"]
        start_y = 240
        spacing = 70

        for i, option in enumerate(options):
            if i == selected_index:
                color = WHITE 
            else:
                color = LIGHT_GREEN

            text = self.menu_font.render(option, True, color)
            rect = text.get_rect(center=(self.screen.get_width() // 2, start_y + i * spacing))
            self.screen.blit(text, rect)


    def draw_settings(self, selected_index: int, music: MusicManager, sound: SoundManager) -> None:
        """
        Dibuja la pantalla de ajustes.

        Args:
            selected_index: índice seleccionado en ajustes.
            music: MusicManager para mostrar estado actual.
            sound: SoundManager para mostrar estado actual.
        """
        self.screen.blit(self.menu_background, (0, 0))

        #darkens the screen
        self.draw_overlay()

        options = [
            f"MUSIC {'ON' if music.is_paused else 'OFF'}",
            f"SOUNDS {'OFF' if sound.is_active else 'ON'}",
            "BACK"
        ]
        
        start_y = 180
        spacing = 70

        for i, option in enumerate(options):
            if i == selected_index:
                color = WHITE 
            else:
                color = LIGHT_GREEN

            text = self.settings_font.render(option, True, color)
            rect = text.get_rect(center=(self.screen.get_width() // 2, start_y + i * spacing))
            
            self.screen.blit(text, rect)
            

    def draw_snake(self, snake: Snake) -> None:
        """
        Dibuja la serpiente en pantalla según su cuerpo (lista de celdas).

        Args:
            snake: instancia Snake con método get_body().
        """
        snake_body = snake.get_body()
        
        for x, y in snake_body:
            rect = pygame.Rect(
                x * GRID_SIZE,
                y * GRID_SIZE,
                GRID_SIZE,
                GRID_SIZE
            )
        
            pygame.draw.rect(self.screen, "green", rect) 
                

    def draw_score(self, score: int) -> None:
        """
        Dibuja el marcador en la esquina superior izquierda.

        Args:
            score: puntuación a mostrar.
        """
        score_text = self.score_font.render(str(score), True, BLACK)
        self.screen.blit(score_text, (10, 10))
       
        
    def draw_playing(self) -> None:
        """Dibuja el fondo del juego (estado playing)."""
        self.screen.blit(self.ingame_background, (0, 0))
        
    
    def draw_overlay(self) -> None:
        """Dibuja una capa semitransparente sobre la pantalla (oscurecer)."""
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 80))
        self.screen.blit(overlay, (0, 0))
