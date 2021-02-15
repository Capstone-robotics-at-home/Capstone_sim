from KeyController import Control
import gym


env = gym.make('Hello-v1')
env.reset()


class Jetbot():
    '''
    Jetbot class for jetbot movement 
    right, left and front are now working 
    back is not working properly 
    DISTANCE, ANGLE, T are the tuning args 
    '''

    DISTANCE = 0.45
    ANGLE = 2
    T = 20

    def right(self):
        print('right')
        for t in range(self.T):
            env.render()
            act = [self.ANGLE, 0] if t % self.T < self.T // 2 else [-self.ANGLE, 0]
            env.step(act)
        return env

    def left(self):
        print('left')
        for t in range(self.T):
            env.render()
            act = [0, self.ANGLE] if t % self.T < self.T // 1.5 else [0, -self.ANGLE]
            env.step(act)
        return env

    def forward(self):
        print('forward')
        for t in range(self.T):
            env.render()
            act = [self.DISTANCE, self.DISTANCE] if t % self.T < (
                self.T // 2) else [-self.DISTANCE, -self.DISTANCE]
            env.step(act)
        return env
 
    def back(self):
        # XXX still under review
        print('backward')
        for t in range(self.T):
            env.render()
            act = [self.DISTANCE, self.DISTANCE] if t % self.T < (
                self.T // 2) else [-self.DISTANCE, -self.DISTANCE]
            env.step(act)
        return env


bot = Jetbot()
c = Control()
c.isCtrling = False

for i in range(5000):
    # action = env.action_space.sample()
    # print(env.action_space)
    env = bot.left()
    # env = bot.right()
    # env = bot.forward()
    # env = bot.back()
    
    while c.isCtrling:
        cmd = c.getdir()
        if cmd == 1: env = bot.forward()
        elif cmd == 2: env = bot.left()
        elif cmd == 3: env = bot.right()
        else:
            print('Lost Control')
            c.isCtrling = False
    env.render()
    


env.close()
