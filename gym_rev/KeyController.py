from pynput.keyboard import Key,Listener


class Control():
    def __init__(self):
        self.dir_ = None #  Make dir as member param. Or it won't be changed in on_press.
        self.isCtrling = True
        print('Press ↑ to start')

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
