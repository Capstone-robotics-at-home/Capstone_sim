import gym
# import mujoco_py

env = gym.make('Hello-v1')
env.reset()

class Jetbot():
    def forward(self):
        '''jetbot going forward action
        t: time to take action 
        distance and T: tuning args  
        return: env'''
        distance = 0.4 
        T = 100
        for t in range(T):
            env.render()
            # act = [distance,0,0] if t % T < (T//4) or t % 100 >= (T//4*3) else - distance
            act = [distance,0,0] if t % T < (T//2) else - distance
            env.step(act)
        return env

    def backward(self):
        distance = 0.4 
        T = 100
        for t in range(T):
            env.render()
            act = [distance,0,0] if t % T < (T//2) else - distance
            env.step(act)
        return env


    def left(self):

        distance = 0.4 
        T = 100
        for t in range(T):
            env.render()
            act = [0,distance,0] if t % T < (T//2) else - distance
            env.step(act)
        return env

    def right(self):

        distance = 0.4 
        T = 100
        for t in range(T):
            env.render()
            act = [0,0,distance] if t % T < (T//2) else - distance
            env.step(act)
        return env

bot = Jetbot()
# env = bot.forward()

for t in range(5000):
    env.render()
    # action = env.action_space.sample()
    # print(env.action_space)
    # env = bot.forward()
    # env = bot.backward()
    env = bot.left()
    # env = bot.right()

env.close()
