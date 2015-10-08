import pygame
import random

class Baddie():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.speed  = 3
        self.color  = color
        self.alive  = True
        return

    def tick(self,back_wall,upper_wall,lower_wall):
        self.new_x = self.x - self.speed
        self.new_y = self.y + random.randint(-1,1)
        if self.new_x < back_wall:
            self.setAlive(False)
        else:
            self.x = self.new_x
        if self.new_y < upper_wall:
            self.new_y = upper_wall
        elif self.new_y + self.height > lower_wall:
            self.new_y = lower_wall - self.height
        self.y = self.new_y
        return self.alive

    def getAlive(self):
        return self.alive

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return
        
