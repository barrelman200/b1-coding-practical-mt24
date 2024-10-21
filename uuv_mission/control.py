class Controller:
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd
        # init error = 0
        self.prev_error = 0
    def compute_control(self, reference: float, observation: float) -> float:
        error = reference - observation
        # u[t] = Kp * e[t] + Kd * (e[t] - e[t-1])
        derivative = error - self.previous_error
        control_action = self.Kp * error + self.Kd * derivative
        self.prev_error = error
        return control_action

