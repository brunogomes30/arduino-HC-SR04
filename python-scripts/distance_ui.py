import pygame

class DistanceUI:

    def __init__(self):
        pass
        
    
    def start(self, width = 640, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont('Arial', 30)
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self, distance):
        self.screen.fill((0, 0, 0))
        text = self.font.render(str(distance), True, (255, 255, 255))
        print(distance)

        max = 200 
        percentage = distance/max

        self.draw_rectangle(self.width/2 - 40, 20 , 80, int(self.height * percentage), (255, 0, 0))
        
        self.screen.blit(text, (self.width/4, self.height/2))
        pygame.display.flip()

    def draw_rectangle(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, (x, y, width, height))

    def close():
        self.running = False
        pygame.quit()