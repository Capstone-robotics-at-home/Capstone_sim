def reader():
    cmd_txt = open('gym_rev/cmd.txt','r')
    cmd = cmd_txt.read(10)
    print('\r',cmd,end=' ')
    cmd_txt.close()

if __name__ == '__main__':
    while True:
        try:
            reader()
        except:
            print('error')