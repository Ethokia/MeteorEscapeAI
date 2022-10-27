import gym

env = gym.make("LunarLander-v2")
env.action_space.seed(42)

observation, info, _, a, b, c, d, e = env.reset()

for _ in range(1000):
    observation, reward, terminated, truncated = env.step(env.action_space.sample())

    if terminated or truncated:
        observation, info, _, a, b, c, d, e = env.reset()

env.close()
