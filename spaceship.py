import pygame
from bullet import Bullet

class Spaceship():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.y_vel = 0
        self.x_vel = 0
        self.on_bottom = False
        self.on_side = False
        self.on_left = False
        self.on_right = False
        return

    def moveLeft(self, dx):
        self.x_vel -= dx

    def moveRight(self, dx):
        self.x_vel += dx

    def jump(self):
        if self.on_bottom == True:
            self.on_bottom = False
            self.y -= 1
            self.y_vel -= 10

        if self.on_left ==True:
            self.y_vel -= 5
            self.x_vel = 5
            self.x += 1
            self.on_left = False
        if self.on_right == True:
            self.y_vel -= 5
            self.x_vel = -5
            self.x -= 1
            self.on_right = False





    def gravity(self):

        if self.y_vel > 10:
            self.y_vel = 10
        if self.y_vel < -10:
            self.y_vel = -10
        if self.on_right ==True or self.on_left ==True  :
            if self.y_vel >= 5:
                self.y_vel -= 1
            if self.y_vel <= 5:
                self.y_vel += 1
            self.y_vel += .01

        else:

            self.y_vel += .3
        self.y += self.y_vel
        return
    def movement(self):


        if self.x < 40:
            self.x = 40
            self.x_vel = 0
            self.on_side = True
            self.on_left = True
        else:
            self.on_side = False
            self.on_left = False

        if self.x > 560:
            self.x = 560
            self.x_vel = 0
            self.on_side = True
            self.on_right = True
        else:
            self.on_side = False
            self.on_right = False
        #x velocity limits
        if self.x_vel > 10:
            self.x_vel = 10
        if self.x_vel < -10:
            self.x_vel = -10
        #slow down if not moving
        if self.x_vel > 0:
            self.x_vel -= .2
        if self.x_vel < 0:
            self.x_vel += .2

        self.x += self.x_vel
        return

    def hitBottom(self, bottom_wall):
        if self.y >= bottom_wall-self.height:
            self.y_vel = 0
            self.y = bottom_wall-self.height
            self.on_bottom = True
        else:
            self.on_bottom = False

    def hitTop(self, top_wall):
        if self.y <= top_wall:
            self.y_vel = 0
            self.y = top_wall

    def tick(self,bottom_wall, top_wall):
        self.movement()
        self.hitBottom(bottom_wall)
        self.hitTop(top_wall)
        self.gravity()

    def fire(self,width,height,color):
        return Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color)
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return
        
