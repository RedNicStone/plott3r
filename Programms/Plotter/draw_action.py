class DrawAction:
    PEN_UP = 1
    PEN_DOWN = 2
    PEN_MOVE = 3

    def __init__(self, t, x=0, y=0):
        self.t = t
        self.x = x
        self.y = y
