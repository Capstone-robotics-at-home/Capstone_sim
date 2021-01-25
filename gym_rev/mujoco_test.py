import gym
import time 
# import mujoco_py

env = gym.make('Hello-v1')
# env = gym.make('Ant-v4')
env.reset()

for t in range(5000):
    env.render()
    # action = env.action_space.sample()
    action = 0.4 if t % 100 < 25 or t % 100 >= 75 else -0.4
        
    # action = 0.5
    env.step(action)

env.close()
