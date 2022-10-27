import math
from shapely.geometry import LineString
from shapely.geometry import Point


class Player:
    x = 0
    y = 0
    dirx = 0
    diry = 0
    color = (255, 0, 0)
    mouse = 0
    speed = 0.25
    ray_length = 0
    nb_rays = 0

    rays = []
    meteors = []

    def __init__(self, x, y, color, mouse, ray_length, nb_rays):
        self.x = x
        self.y = y
        self.color = color
        self.mouse = mouse
        self.ray_length = ray_length
        self.nb_rays = nb_rays

        self.rays_init()

    def draw(self, pygame, screen, meteors):
        self.meteors = meteors
        # self.dirx = (self.get_mouse_pos()[0] - self.x) / 10
        # self.diry = (self.get_mouse_pos()[1] - self.y) / 10

        self.x += self.dirx
        self.y += self.diry

        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
        self.draw_rays(pygame, screen, meteors, False)

    def inputs(self):
        inputs = []
        for ray in self.rays:
            inputs.append(int(ray.collision_detected))
        return inputs

    def get_mouse_pos(self):
        return self.mouse.get_pos()

    def reset_movement(self):
        self.dirx = 0
        self.diry = 0

    def move_up(self):
        self.reset_movement()
        self.diry = -self.speed

    def move_down(self):
        self.reset_movement()
        self.diry = self.speed

    def move_right(self):
        self.reset_movement()
        self.dirx = self.speed

    def move_left(self):
        self.reset_movement()
        self.dirx = -self.speed

    def isDead(self):
        p_player = Point(self.x, self.y)
        c_player = p_player.buffer(10).boundary
        
        for m in self.meteors:
            p_meteor = Point(m.x, m.y)
            c_meteor = p_meteor.buffer(10).boundary
            if c_player.intersection(c_meteor):
                return True

        return False

    def rays_init(self):
        t = 0
        for i in range(self.nb_rays):
            t = t + math.pi / (self.nb_rays / 2)
            x = self.ray_length * math.cos(t + math.pi)
            y = self.ray_length * math.sin(t + math.pi)
            self.rays.append(Ray((self.x, self.y), (self.x + x, self.y + y), self.color))

    def draw_rays(self, pygame, screen, meteors, show):
        t = 0
        for i in range(self.nb_rays):
            t = t + math.pi / (self.nb_rays / 2)
            x = self.ray_length * math.cos(t + math.pi)
            y = self.ray_length * math.sin(t + math.pi)
            self.rays[i].center = (self.x, self.y)
            self.rays[i].endpoint = (self.x + x, self.y + y)
            if show:
                self.rays[i].draw(pygame, screen)
            self.rays[i].is_colliding(meteors)


class Ray:
    center = (0, 0)
    endpoint = (0, 0)
    color = 0
    collision_detected = False

    def __init__(self, center, endpoint, color):
        self.center = center
        self.endpoint = endpoint
        self.color = color

    def draw(self, pygame, screen):
        pygame.draw.line(screen, (255, 0, 0) if self.collision_detected else self.color, self.center, self.endpoint, 1)

    def is_colliding(self, meteors):
        self.collision_detected = False
        for i in range(meteors.__len__()):

            i = int(i)
            xa = self.center[0]
            ya = self.center[1]
            xb = self.endpoint[0]
            yb = self.endpoint[1]

            xc = meteors[i].x
            yc = meteors[i].y

            p = Point(xc, yc)
            c = p.buffer(10).boundary
            l = LineString([(xa, ya), (xb, yb)])
            inter = c.intersection(l)

            is_colliding = not inter.is_empty

            if is_colliding:
                self.collision_detected = True
