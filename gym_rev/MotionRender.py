import gym
import time  

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

    def step_by_cmd(self):
        """ Read the com.txt, render the motion """
        cmd_txt = open('gym_rev/cmd.txt','r')
        cmd = cmd_txt.read(10)
        if cmd == 'left':
            self.left()
            time.sleep(1)
        elif cmd == 'right':
            self.right()
            time.sleep(1)
        elif cmd == 'forward':
            self.forward() 
            time.sleep(1)
        elif cmd == '0':
            print('Waiting')
            self.env.render()
        else:
            print('wrong command')
            raise ValueError('Invalid string of command')

    def demo_motion(self):
        """ simple demo motion like turn left, right, go forward """
        for _ in range(100):
            self.right()           



if __name__ == '__main__':
    mRender = MotionRender() 
    # mRender.demo_motion()  
    mRender.right()
    while True:
        mRender.step_by_cmd()
    mRender.quit() 
    

    
     

