from pygame import Surface
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def load_image(filepath: str) -> Surface:
    """
    Carga una imagen desde disco y la escala a las dimensiones de la pantalla.

    Args:
        filepath: ruta al archivo de imagen.

    Returns:
        Surface: Surface de pygame con la imagen cargada y escalada.

    Raises:
        FileNotFoundError: si pygame no puede cargar la imagen.
    """
    image = None
    
    try:
        image = pygame.image.load(filepath).convert()
        
        image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            
    except pygame.error:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {filepath}")
        
    return image