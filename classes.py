import random

class Rect:
    def __init__(self, x, y, w, h, vx, vy, f, s):
        self.x = x-w/2
        self.y = y-h/2
        self.w = w
        self.h = h
        self.s = 1
        self.vx = vx
        self.vy = vy
        if self.vx < 2: self.vx -= 4
        if self.vy < 2: self.vy -= 4
        if(self.vx == 0): self.vx = random.randint(-1, 1)
        if(self.vy == 0): self.vy = random.randint(-1, 1)
        self.fill = f
        self.stroke = s
    def move(self, other, n):
        self.x += self.vx/(n+1)
        self.y += self.vy/(n+1)

        if self.x > 600-self.w*self.s:
            self.vx = -self.vx
            self.x = 600-self.w*self.s
        if self.x < 0:
            self.vx = -self.vx
            self.x = 0
        if self.y > 600-self.h*self.s:
            self.vy = -self.vy
            self.y = 600-self.h*self.s
        if self.y < 0:
            self.vy = -self.vy
            self.y = 0
    def col(self, other):
        self.vx, other.vx = other.vx, self.vx
        self.vy, other.vy = other.vy, self.vy
        #if abs(self.rect.right > other.rect.left) < abs(self.rect.bottom-other.rect.top) or abs(self.rect.left < other.rect.right) < abs(self.rect.top < other.rect.bottom):
        if abs(self.x-other.x)/(self.w/2+other.w/2) < abs(self.y-other.y)/(self.h/2+other.h/2):
            #self.vx = abs(self.vx)
            #other.vx = abs(other.vx)
            if self.x > other.x:
                #other.vy = -other.vy
                self.rect.right = other.rect.left
                #self.x = other.x+other.w/2+self.w/2+1
            else: 
                #self.vy = -self.vy
                self.rect.left = other.rect.right
                #self.x = other.x-other.w/2-self.w/2-1
            #self.vy = -self.vy
            #other.vy = -other.vy
            
            # shrink other
            other.s -= 0.1
            other.x += other.w/10/2
            other.y += other.h/10/2
        else:
            #self.vy = abs(self.vy)
           # other.vy = abs(other.vy)
            if self.y > other.y:
                #other.vx = -other.vx
                self.rect.bottom = other.rect.top
                #self.y = other.y+other.h/2+self.h/2+1
            else:
                #self.vx = -self.vx
                self.rect.top = other.rect.bottom
                #self.y = other.y-other.h/2-self.h/2-1
            #self.vx = -self.vx
            #other.vy = -other.vx
            

            # shrink self
            self.s -= 0.1
            self.x += self.w/10/2
            self.y += self.h/10/2