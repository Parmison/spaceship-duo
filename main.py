import pygame
pygame.init()

space = pygame.image.load("lesson 6/image/space bg.png")
yellow_ship = pygame.image.load("lesson 6/image/spaceship yellow.png")
orange_ship = pygame.image.load("lesson 6/image/spaceship orange.png")

screen = pygame.display.set_mode((1250,690))

border = pygame.Rect(625,0,5,690)

#pygame.sprite.Sprite

class spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super().__init__()
        self.color = color
        if color == "yellow":
            self.image = pygame.transform.rotate(yellow_ship,90)
        elif color == "orange":
            self.image = pygame.transform.rotate(orange_ship,270)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.health = 100

orange = spaceship(950,330,"orange")
yellow = spaceship(350,330,"yellow")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"white",border)
    screen.blit(orange.image,orange.rect.center)
    screen.blit(yellow.image,yellow.rect.center)
    pygame.display.update()
