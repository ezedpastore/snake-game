import pygame

class MusicManager:
    """
    Gestor para la música de fondo usando pygame.mixer.music.
    Provee métodos para pausar/continuar y detener la música.
    """
    is_paused: bool
    
    def __init__(self, path: str) -> None:
        """
        Inicializa y reproduce la pista de música en bucle.

        Args:
            path: ruta al archivo de música.
        """
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        
        self.is_paused = False

    def music_on(self) -> None:
        """Reanuda la música si estaba pausada."""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
    
    def music_off(self) -> None:
        """Pausa la música si está sonando."""
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            
    def quit(self) -> None:
        """Detiene la reproducción de música (cleanup)."""
        pygame.mixer.music.stop()

