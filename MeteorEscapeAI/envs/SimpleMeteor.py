from MeteorEscapeAI.envs.Meteor import Meteor
import random
import MeteorEscapeAI.envs.Config as Config


class SimpleMeteor(Meteor):

    def __init__(self, player):
        side = random.randint(0, 3)
        x = 0
        y = 0

        if side == 0 :
                x = 0
                y = random.randint(0, Config.HEIGHT)
        elif side == 1 :
                x = Config.WIDTH
                y = random.randint(0, Config.HEIGHT)
        elif side == 2 :
                x = random.randint(0, Config.WIDTH)
                y = 0
        elif side == 3 :
                x = random.randint(0, Config.WIDTH)
                y = Config.HEIGHT

        super().__init__(x, y, player, (255, 0, 0))
