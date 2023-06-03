from turtle import Turtle
START_POSITION = [ (0, 0), (-10, 0), (-20, 0), (-30, 0) ]
START_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self .head=self.segments[0]
    def create_snake(self):
        for pos in START_POSITION:
             self.add_snake(pos)
    def add_snake(self,pos):
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.goto(pos)
            self.segments.append(t)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend_snake(self):
        self.add_snake(self.segments[-1].position())
    def  move(self):
        for seg_pos in range(len(self.segments)-1,0,-1):
                new_x=self.segments[seg_pos-1].xcor()
                new_y=self.segments[seg_pos - 1].ycor()
                self.segments[seg_pos].goto(new_x,new_y)
        self.head.fd(START_DIST)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)