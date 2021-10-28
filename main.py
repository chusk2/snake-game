import time
from turtle import Turtle, Screen
from snake import Snake


class Game:
    def __init__(self, snake_size=3, canvas_size=300, canvas_color='black'):
        # create a screen
        self.scr = Screen()
        self.scr.setup(height=canvas_size + 50, width=canvas_size + 50)
        self.scr.bgcolor(canvas_color)
        self.scr.title('Snake Game')
        self.scr.tracer(0)
        self.size = canvas_size
        self.snk = Snake(snake_size, canvas_size)
        self.game_is_on = None
        self.score = 0
        #self.food = Food(self.size)

    def draw_margins(self):
        margin = Turtle()  # turtle to draw margins
        margin.pencolor('blue')
        margin.pensize(2)
        # set turtle in left upper corner
        margin.penup()
        margin.goto(-self.size, self.size)  # left upper corner
        margin.pendown()
        for _ in range(4):
            margin.forward(self.size * 2)
            margin.right(90)
        margin.hideturtle()
        self.scr.update()

    def draw_grid(self):
        
        number_turtles = 2 * (self.size // 20)
        for i in range(number_turtles+1):  # +1 to fill the borders of grid
            x_t = Turtle()  # turtle to draw horizontal lines
            y_t = Turtle()  # turtle to draw vertical lines
            x_t.pencolor('gray')
            y_t.pencolor('gray')
            # set turtles in their starting positions without painting
            x_t.penup()
            y_t.penup()
            # starting positions
            y_t.goto(-self.size + 20 * i, -self.size)  # vertical lines
            y_t.write(-self.size + 20 * i)
            x_t.goto(-self.size, -self.size + 20 * i)  # horizontal lines
            x_t.pendown()
            y_t.pendown()
            # draw lines until end of canvas
            x_t.goto(self.size, x_t.ycor())
            y_t.goto(y_t.xcor(), self.size)
            x_t.hideturtle()
            y_t.hideturtle()
    
        self.scr.update()

    def check_eaten_food(self):
        snake_head_position = self.snk.pieces[0].position()
        if self.food.eaten_food(snake_head_position):
            self.score += 10
            print(f'Apple eaten! Your score is: {self.score}')

    def listen_to_keys(self):
        # Event listeners
        self.scr.onkeypress(lambda: self.snk.turn_snake('up'), 'Up')
        self.scr.onkeypress(lambda: self.snk.turn_snake('down'), 'Down')
        self.scr.onkeypress(lambda: self.snk.turn_snake('left'), 'Left')
        self.scr.onkeypress(lambda: self.snk.turn_snake('right'), 'Right')
        self.scr.onkeypress(self.snk.return_position, 'p')
        self.scr.onkeypress(self.snk.apple.return_position, 'f')
        self.scr.onkeypress(self.paused_mode, 'space')
        # self.scr.onkeypress(self.pause, 'space')
        self.scr.listen()

    def paused_mode(self):
        self.check_eaten_food()
        self.snk.move()
        self.scr.update()
        time.sleep(0.1)

    def start(self):
        # start the game
        self.game_is_on = True
        self.draw_margins()
        self.draw_grid()
        self.listen_to_keys()
        self.scr.update()

        while self.game_is_on:
            #self.check_eaten_food()
            self.snk.move()
            self.scr.update()
            time.sleep(0.1)

    # def pause(self):
    #     if self.game_is_on:
    #         self.game_is_on = False
    #     elif not self.game_is_on:
    #         self.game_is_on = True


game = Game(snake_size=4, canvas_size=160, canvas_color='white')
game.start()

game.scr.exitonclick()

