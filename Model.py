'''CS 108 Final Project - Single Player Pong

@author: Alina Sainju
@Semester: Spring, 2023

'''

from random import randint 

class Game:
    
    def __init__(self, x1 = 400, y1 = 400, x2 = 490, y2 = 410, vel_x = 0, vel_y = 0, bar_vx1 = 0, bar_vx2 = 0, cx =0, cy = 0, radius = 10):
        '''Instantiates a new game.'''
        self.x1, self.y1 = x1,y1 
        self.x2, self.y2 = x2, y2
        self.vel_x, self.vel_y = vel_x, vel_y
        self.bar_vx1, self.bar_vx2 = bar_vx1, bar_vx2
        self.cx, self.cy = cx, cy 
        self.radius = radius
        self.score = 0
        
        score = open("topscore.txt", "r")
        self.maxscore = int(score.readline()) #Reads the initial top score. 
        score.close()
        
    def draw_bar(self, drawing):
        '''Creates the rectangular bar.'''
        drawing.rectangle(self.x1, self.y1, self.x2, self.y2)
        
    def move_bar(self, event):
        '''Allows the rectangular bar to move left and right.'''
        if event.key == "d":
            if self.x2 < 500:
                self.x1 += self.bar_vx1
                self.x2 += self.bar_vx2
        if event.key == "a":
            if self.x1 > 0:
                self.x1 -= self.bar_vx1
                self.x2 -= self.bar_vx2
     
    def draw_ball(self, drawing):
        '''Creates the circular ball.'''
        drawing.oval(self.cx - self.radius,
             self.cy - self.radius,
             self.cx + self.radius,
             self.cy + self.radius)
        
    def engine(self, drawing, window):
        '''Regulates the movement of the ball.'''
        #Moves the ball.
        self.cx += self.vel_x
        self.cy += self.vel_y
        
        #Bounces the ball off of the borders. 
        if self.cx + self.radius > drawing.width or self.cx - self.radius < 0:
            self.vel_x *= -1
        if self.cy + self.radius > drawing.height  or self.cy - self.radius < 0:
            self.vel_y *= -1
        
        #Bounces the ball off of the rectangular bar. 
        if self.cy + self.radius > self.y1 and self.cy + self.radius < self.y2:
            if self.cx + self.radius >= self.x1 and self.cx + self.radius <= (self.x1+ self.x2)/2: 
                self.vel_x *= -1
                self.vel_y *= -1
                self.score += 1
            
            if self.cx + self.radius <= self.x2 and self.cx + self.radius >= (self.x1+ self.x2)/2:
                self.vel_x *= 1
                self.vel_y *= -1
                self.score += 1
                
        #Freezes the ball once it touches the bottom, aka ends the game.
        if self.cy +self.radius >= 500:
            self.vel_x = 0
            self.vel_y = 0
            if self.score > self.maxscore: #Compares the player's current score to the top score and updates the top score.
                score = open("topscore.txt", "w")
                score.write(str(self.score))
                score.close()
            self.cy = 0
            window.hide()
        
        
        drawing.text(350, 458, "Your score:" + str(self.score)) #Displays the player's current score real time.
        drawing.text(350, 475, "Top score:" + str(self.maxscore)) #Displays the top score.
      
        

    def update_currentgame(self, vel_x, vel_y, vx1, vx2):
        '''Updates game parameters depending on difficulty level each time the game is started.'''
        #Changes the difficulty level.
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.bar_vx1 = vx1
        self.bar_vx2 = vx2
        
        #Restarts the game.
        self.cx = randint(6,490)
        self.cy = randint(6,100)
        self.score = 0
        score = open("topscore.txt", "r")
        self.maxscore = int(score.readline())
        score.close()
        
        
            
            
            
        
            
        
        