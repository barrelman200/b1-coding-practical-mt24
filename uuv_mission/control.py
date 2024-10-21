class Controller:
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd
        # init error = 0
        self.prev_error = 0


