import gym

import GameLoop


def main():
    env = gym.make("MeteorEscapeAI-v1")

    env.reset()

    GameLoop.game_loop()

if __name__ == '__main__':
    main()

