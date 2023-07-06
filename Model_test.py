'''CS 108 Final Project - Single Player Pong

This module tests some basic functionality of the single player pong game.

@author: Alina Sainju
@Semester: Spring, 2023

'''



from Model import Game

#Testing that the constructor correctly assigns values. 
game1 = Game(x1 = 412,y1= 424,x2= 493,y2 = 430,vel_x = 2,vel_y = 5, bar_vx1= 3, bar_vx2 = 7,cx=3,cy=3, radius = 11)
assert game1.x1 == 412
assert game1.y1 == 424
assert game1.x2 == 493
assert game1.y2 == 430
assert game1.vel_x == 2
assert game1.vel_y == 5
assert game1.bar_vx1 == 3
assert game1.bar_vx2 == 7
assert game1.cx == 3
assert game1.cy == 3
assert game1.radius == 11

#Testing that the values are being updated.
game1.update_currentgame(3,4,6,7)
assert game1.vel_x == 3
assert game1.vel_y == 4
assert game1.bar_vx1 == 6
assert game1.bar_vx2 == 7


