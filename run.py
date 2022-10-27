import MeteorEscapeAI
import gym

env = gym.make('MeteorEscapeAI-v1')


for i in range(1000):
    env.step()
    env.render()
