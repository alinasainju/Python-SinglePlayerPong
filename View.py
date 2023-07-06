'''CS 108 Final Project - Single Player Pong

@author: Alina Sainju
@Semester: Spring, 2023

@Features added since Project 3:
- Changed the name of move_ball() and place_ball() to engine() and update_currentgame() respectively in Game class.
- Added file handling code in the constructor method of Game class.
- Updated the file handling code in the engine() method of Game class.
- Added code in update_currentgame() of Game class that randomizes the position of the ball every time
  the game is restarted.
- Added difficulty levels in Simulator class along with buttons that allow user to choose level.
- Updated name of the game application from "guizero" to "Single Player Pong".
- Wrote tests to test some functionality of the Game. 
- Documented code. 


'''

from Model import Game
from guizero import App, Drawing, PushButton, Window, Text, ButtonGroup  

class Simulator:
    
    def __init__(self, app):
        '''Instantiates the game driver.'''
        def open_window():
            '''Sets game difficulty.'''
            if difficulty.value_text == "Easy":
                self.game.update_currentgame(2,2,15,15)
            elif difficulty.value_text == "Medium":
                self.game.update_currentgame(3,3,20,20)
            elif difficulty.value_text == "Hard":
                self.game.update_currentgame(5,5,35,35)
            self.window.show()
            
        def close_window():
            self.window.hide()
            
        self.window = Window(app)
        self.window.hide()
        
        app.title = "Single Player Pong"
        self.window.title = "Single Player Pong"
        difficulty = ButtonGroup(app, options = ["Easy", "Medium", "Hard"], selected = "Easy")
        start_button = PushButton(app, text = "Start", command = open_window)
        quit_button = PushButton(app, text = "Exit Game", command = app.destroy)
        
            
        self.drawing = Drawing(self.window, width = 500, height = 500)
        self.game = Game()
        self.window.repeat(10, self.draw_frame)
        
        self.window.when_key_pressed = self.game.move_bar
    
        
        
    def draw_frame(self):
        '''Draws each frame of the different elements of the game: bar and ball.
            Also calls engine() to regulate ball movement in each frame.'''   
        self.drawing.clear()
        self.game.draw_bar(self.drawing)
        self.game.draw_ball(self.drawing)
        self.game.engine(self.drawing, self.window)
    
        
app = App()
simulator = Simulator(app)
app.display()
        
        
