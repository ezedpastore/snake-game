class Snake:
    """
    Representación simple de la serpiente:
    - _body: lista de celdas (x, y) donde 0 es la cabeza.
    - _direction: vector de dirección en celdas.
    - _score: contador de crecimiento/puntos.
    """
    body: list[tuple[int, int]]
    direction: tuple[int, int]
    score: int
    
    def __init__(self) -> None:
        """
        Inicializa la serpiente con posición y dirección por defecto.
        """
        self._body = [
            (12, 10), 
            (11, 10)
        ]
        self._direction = (1, 0)
        self._score = 0
        
        
    def insert(self) -> None:
        """
        Inserta una nueva cabeza en la dirección actual (no elimina la cola).
        Operación interna usada por move_snake y grow_snake.
        """
        new_head = (self._body[0][0] + self._direction[0], self._body[0][1] + self._direction[1])
        
        self._body.insert(0, new_head)
        
        
    def move_snake(self) -> None:
        """
        Mueve la serpiente una celda en la dirección actual:
        inserta nueva cabeza y elimina la última celda (cola).
        """
        self.insert()
        self._body.pop()
        
        
    def grow_snake(self) -> None:
        """
        Aumenta la serpiente (se mueve sin eliminar la cola) y suma 1 punto al score.
        """
        self.insert()
        self._score += 1
        
        
    def update_direction(self, new_direction: tuple[int, int]) -> None:    
        """
        Actualiza la dirección si la nueva no es la opuesta (evita invertir 180º).

        Args:
            new_direction: vector (dx, dy) de la nueva dirección.
        """
        if(new_direction != (-self._direction[0], -self._direction[1])):
            self._direction = new_direction
            
    
    def get_body(self) -> list[tuple[int, int]]:
        """
        Devuelve la lista de celdas que componen la serpiente (lectura).
        """
        return self._body
    
    
    def get_score(self) -> int:
        """
        Devuelve la puntuación actual.
        """
        return self._score