from gym.envs.registration import register

register(id='MeteorEscapeAI-v1',
        entry_point='MeteorEscapeAI.envs:MeteorEnv'
        )
