from gym_rev.MotionRender import MotionRender
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/gym_rev")

if __name__ == '__main__':
    mRender = MotionRender()
    for _ in range(10):
        mRender.left()
    for _ in range(10):
        mRender.right()
    for _ in range(10):
        mRender.forward()
    mRender.quit()
