import math

class Ease:
    def __init__(self,
                 miliseconds,
                 function,
                 max_value,
                 loop = False):
        self.easing = True
        self.ms = miliseconds
        self.funct= function
        self.time = 0
        self.loop = loop
        self.max = max_value
        self.val = 0
    def update(self, dt):
        if self.easing:
            self.time += dt
            if self.time > self.ms:
                if self.loop:
                    self.time = 0
                else:
                    self.easing = False
            else:
                x = self.time / self.ms
                self.val = self.funct(x) * self.max
    def restart(self):
        self.easing = True
        self.time = 0

def sinEaseIn(x):
    return math.sin(math.pi * x)

def inOutBack(x):
    c1 = 1.70158;
    c2 = c1 * 1.525;

    if x < 0.5:
      return (pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2
    else:
      return (pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2;

