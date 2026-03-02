import pygame

class SoundManager:
    """
    Gestor sencillo de efectos de sonido.
    Mantiene una referencia a un Sound de pygame y un flag is_active.
    """
    is_active: bool
    
    def __init__(self, path: str) -> None:
        """
        Crea el SoundManager y carga el efecto de sonido.

        Args:
            path: ruta al archivo de sonido.
        """
        self.sound = pygame.mixer.Sound(path)
        self.is_active = True

    def sound_off(self) -> None:
        """Desactiva los efectos (no los reproduce)."""
        self.is_active = False
        
    def sound_on(self) -> None:
        """Activa los efectos para que se puedan reproducir."""
        self.is_active = True
        
    def play_sound(self) -> None:
        """Reproduce el efecto si está activo."""
        if self.is_active:
            self.sound.play()
    
    def quit(self) -> None:
        """Detiene el sonido (cleanup)."""
        self.sound.stop()

