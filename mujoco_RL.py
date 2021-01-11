import gym 
# import mujoco_py

env = gym.make('Ant-v3')
env.reset()
for _ in range(5000):
    env.render()
    env.step(env.action_space.sample())
env.close()

