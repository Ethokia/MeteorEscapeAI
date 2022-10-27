import MeteorEscapeAI
import gym


def main():
    env = gym.make("MeteorEscapeAI-v1")

    for _ in range(100):
        env.reset()
        while not env.game_loop.player.isDead():
            env.step(env.action_space.sample())
            env.render()

    print("Closing Environment")
    env.close()

if __name__ == '__main__':
    main()
