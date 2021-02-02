import gym
from pynput.keyboard import Key,Listener

env = gym.make('Hello-v1')
env.reset()

class Control():
    def __init__(self):
        self.dir_ = None # dir一定要用成员变量，不然没办法在on_press中修改

    def getdir(self):
        self.dir_ = None    # 如果是不是上下左右则返回None
        def on_press(key):
            if key == Key.up:self.dir_ = 1
            elif key == Key.down:self.dir_ = 4
            elif key == Key.left:self.dir_ = 2
            elif key == Key.right:self.dir_ = 3
            return False
        listener = Listener(on_press=on_press) # 创建监听器
        listener.start()    # 开始监听，每次获取一个键
        listener.join()     # 加入线程
        listener.stop()     # 结束监听，没有这句也行，直接随函数终止
        return self.dir_ 

class Jetbot():
    '''
    Jetbot class for jetbot movement 
    right, left and front are now working 
    back is not working properly 
    DISTANCE, ANGLE, T are the tuning args 
    '''

    DISTANCE = 0.4
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
            act = [0, self.ANGLE] if t % self.T < (
                self.T // 2) else [0, -self.ANGLE]
            env.step(act)
        return env

    def front(self):
        print('2-wheel-front')
        for t in range(self.T):
            env.render()
            act = [self.DISTANCE, self.DISTANCE] if t % self.T < (
                self.T // 2) else [-self.DISTANCE, -self.DISTANCE]
            env.step(act)
        return env

    def back(self):
        print('2-wheel-back')
        for t in range(self.T):
            env.render()
            act = [self.DISTANCE, self.DISTANCE] if t % self.T < (
                self.T // 10) else [-self.DISTANCE, -self.DISTANCE]
            env.step(act)
        return env

    def cont_left(self):
        # XXXX
        print('left continuously')
        for t in range(self.T):
            env.render()
            act = [self.ANGLE, 0]
            env.step(act)
        return env


bot = Jetbot()
# env = bot.forward()

for i in range(5000):
    env.render()
    # action = env.action_space.sample()
    # print(env.action_space)
    # env = bot.front()
    # env = bot.left()
    # env = bot.right()
    # env = bot.back()
    # env = bot.cont_left()

    c = Control()
    i = 0
    while True:
        cmd = c.getdir()
        if cmd == 1:
            env = bot.front()
        elif cmd == 2:
            env = bot.left()
        elif cmd == 3:
            env = bot.right()
        else:
            print('something wrong')

env.close()
