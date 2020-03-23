import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initializa the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right:
            # Si toca pared derecha, nave para pared izquierda
            if self.rect.right > (self.screen_rect.right - 2):
                self.x = (self.screen_rect.left)
            # Si no toca pared derecha, nave mueve derecha
            else:
                self.x += self.settings.ship_speed
        # Usamos otro if para que se comprueben las dos condiciones
        # Si usamos elif y presionamos <- y ->, ganaría derecha porque va primero
        if self.moving_left:
            # Si toca pared izquierda, nave para pared derecha
            if self.rect.left < (self.screen_rect.left + 2):
                self.x = (self.screen_rect.right - 50)
            # Si no toca parec izquierda, nave mueve izquierda
            else:
                self.x -= self.settings.ship_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)