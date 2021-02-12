import gym 

env = gym.make('Hello-v1')

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
            act = [0, self.ANGLE] if t % self.T < (
                self.T // 2) else [0, -self.ANGLE]
            env.step(act)
        return env

    def front(self):
        print('forward')
        for t in range(self.T):
            env.render()
            act = [self.DISTANCE, self.DISTANCE] if t % self.T < (
                self.T // 2) else [-self.DISTANCE, -self.DISTANCE]
            env.step(act)
        return env

    def back(self):
        print('backward')
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