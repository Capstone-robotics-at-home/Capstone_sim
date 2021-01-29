import gym
# import mujoco_py

env = gym.make('Hello-v1')
env.reset()

class Jetbot():
    def forward(self,t):
        '''jetbot going forward action at time t
        t: time to take action 
        distance and T: tuning args  
        return: action'''
        distance = 0.4 
        T = 100
        act = distance if t % T < (T//4) or t % 100 >= (T//4*3) else - distance
        return act

bot = Jetbot()


for t in range(5000):
    env.render()
    # action = env.action_space.sample()
    print(env.action_space)
    action = bot.forward(t)
    # action = 0.4 if t % 100 < 25 or t % 100 >= 75 else -0.4
        
    # action = 0.5
    env.step(action)

env.close()
