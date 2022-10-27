import pygame
from pygame.time import Clock

import MeteorEscapeAI.envs.Config as Config
from MeteorEscapeAI.envs.SimpleMeteor import SimpleMeteor
from MeteorEscapeAI.envs.Player import Player


class GameLoop:
    running = True

    x = 50
    y = 50
    score = 0

    player = None
    meteors = []
    screen = None

    clock = Clock()
    compteur = 60
    gen_nb = 0

    # x et y represente le point de depart du joueur
    def __init__(self, x, y, gen_nb):
        self.x = x
        self.y = y
        self.gen_nb = gen_nb
        self.player = Player(x, y, (0, 255, 0), pygame.mouse, 200, 16)
        self.meteors = []
	
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Meteor Escape AI")

    def render(self):
        self.clock.tick(120)
        self.screen.fill((255, 255, 255))
        self.player.draw(pygame, self.screen, self.meteors)
        for m in self.meteors:
            m.draw(pygame, self.screen)
            if m.is_out_of_screen():
                self.meteors.remove(m)

        font = pygame.font.SysFont(None, 24)
        img = font.render('Generation : ' + str(self.gen_nb), True, (0, 0, 0))
        self.screen.blit(img, (20, 20))
        pygame.display.update()


    def step(self):
        self.score+=1
        self.compteur -= 1

        if self.compteur <= 0:
            self.compteur = 60
            self.meteors.append(SimpleMeteor(self.player))

        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.QUIT:
                running = False

