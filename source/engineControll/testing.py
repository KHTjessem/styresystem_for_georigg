from controll import controll


class testing:
    def __init__(self):
        self.c = controll()

    def getTall(self, msg):
        return int(input(msg))

    def stop(self):
        self.c.stop()
    def close(self):
        self.c.close()
    
    
    def start(self):
        while True:
            valg = self.meny()
            if not self.run_command(valg):
                break
            
    def meny(self):
        print('Commands:')
        print('0: quit')
        print('1: rotate right')
        print('2: rotate left')
        print('3: stop')
        return self.getTall('Input number of wanted action: ')
    
    def run_command(self, valg):
        if valg == 0:
            return False
        elif valg == 1:
            vel = self.getTall('Choose speed(1-1000): ')
            self.c.rotate_right(vel)
        elif valg == 2:
            vel = self.getTall('Choose speed(1-1000): ')
            self.c.rotate_left(vel)
        elif valg == 3:
            self.c.stop()
        return True


if __name__ == "__main__":
 t = testing()
 t.start()
 t.stop()
 t.close()
