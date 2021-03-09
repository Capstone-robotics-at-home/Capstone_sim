import gym 

class MotionRender(): 
    ''' Jetbot simulation render for each step '''
    def __init__(self): 
        self.env = gym.make('Hello-v1')
        self.env.reset() 
        self.DISTANCE = 0.45 
        self.ANGLE = 2 
        self.T = 20 

    def right(self):
        print('right') 
        for t in range(self.T):
            self.env.render()
            act = [self.ANGLE, 0] if t % self.T < self.T // 2 else [-self.ANGLE, 0]
            self.env.step(act)
            self.env.render() 

    def left(self):
        print('left')
        for t in range(self.T):
            self.env.render()
            act = [0, self.ANGLE] if t % self.T < self.T // 1.5 else [0, -self.ANGLE]
            self.env.step(act)
            self.env.render() 

    def forward(self):
        print('forward')
        for t in range(self.T):
            self.env.render()
            act = [self.DISTANCE, self.DISTANCE] if t % self.T < (
                self.T // 2) else [-self.DISTANCE, -self.DISTANCE]
            self.env.step(act)
            self.env.render() 
 

    def quit(self):
        self.env.close() 
    


if __name__ == '__main__':
    mRender = MotionRender() 
    for _ in range(10):
        mRender.left() 
    for _ in range(10):
        mRender.right() 
    for _ in range(10):
        mRender.forward() 
    mRender.quit() 

    

    
     

