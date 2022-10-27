import MeteorEscapeAI.envs.Config as Config

class Meteor:
    # class attribute
    x = 0
    y = 0
    dirx = 0
    diry = 0
    radius = 10
    color = (255, 0, 0)

    def __init__(self, x, y, player, color):
        self.x = x
        self.y = y
        self.dirx = (player.x - x) / 100
        self.diry = (player.y - y) / 100
        self.color = color

    def draw(self, pygame, screen):
        self.x += self.dirx
        self.y += self.diry
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_out_of_screen(self):
        return self.x <= -self.radius or self.x >= Config.WIDTH or self.y <= -self.radius or self.y >= Config.HEIGHT
