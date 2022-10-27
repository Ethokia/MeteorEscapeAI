import gym
from gym import spaces
import pygame
import numpy as np

from MeteorEscapeAI.envs.GameLoop import GameLoop

class MeteorEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 60}
    game_loop = None
    player_location = None
    gen_nb = 0

    def __init__(self, render_mode=None):
        self.window_size = 512  # The size of the PyGame window

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        self.observation_space = spaces.Discrete(16) #nb_rays

        # We have 4 actions, corresponding to "right", "up", "left", "down"
        self.action_space = spaces.Discrete(4)

        """
        The following dictionary maps abstract actions from `self.action_space` to 
        the direction we will walk in if that action is taken.
        I.e. 0 corresponds to "right", 1 to "up" etc.
        """
        self._action_to_direction = {
            0: np.array([4, 0]), # UP
            1: np.array([0, 4]), # RIGHT
            2: np.array([-4, 0]), # DOWN
            3: np.array([0, -4]), # LEFT
        }

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        """
        If human-rendering is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None

    def reset(self, seed=None, options=None):
        self.gen_nb += 1

        self.player_location = np.ones(2)
        self.player_location *= self.window_size/2

        self.game_loop = GameLoop(self.player_location[0], self.player_location[1], self.gen_nb)

        observation = self.game_loop.player.inputs()
        info = None

        if self.render_mode == "human":
            self.render()

        return observation, info

    def step(self, action):
        direction = self._action_to_direction[action]

        self.player_location = np.clip(self.player_location + direction, 0, self.window_size-1)
        self.game_loop.player.x = self.player_location[0]
        self.game_loop.player.y = self.player_location[1]

        self.game_loop.step()

        terminated = self.game_loop.player.isDead()

        reward = self.game_loop.score

        observation = self.game_loop.player.inputs()
        info = None

        if self.render_mode == "human":
            self.render()

        return observation, reward, terminated, False, info

    def render(self):
        self.game_loop.render()

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
