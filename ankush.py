import turtle 
import time
import random


delay = 0.1
queue =[]


pen = turtle.Turtle()
pen.shape('circle')
pen.penup()
pen.speed(0)
pen.color('White')

pen.hideturtle()
pen.goto(0,225)
pen.write("Score: 0    High score: 0   ",align='center',font=('Arial',15,'italic'))


window = turtle.Screen()
window.bgcolor('Black')
window.title('Snake_Game: Ankush Garg')
window.setup(width=1000,height=500)
window.tracer(0)


Snake_Head = turtle.Turtle()
Snake_Head.speed(0)
Snake_Head.shape('circle')
Snake_Head.color('red')
Snake_Head.penup()
Snake_Head.goto(0,0)
Snake_Head.direction ='stop'


Snake_Food = turtle.Turtle()
Snake_Food.speed(150)
Snake_Food.shape('circle')

Snake_Food.color('yellow')
Snake_Food.penup()
Snake_Food.goto(0,150)



def Move_Snake():
    if Snake_Head.direction == 'up':
        y = Snake_Head.ycor()
        Snake_Head.sety(y + 10)
    if Snake_Head.direction == 'down':
        y = Snake_Head.ycor()
        Snake_Head.sety(y - 10)
    if Snake_Head.direction == 'left':
        x = Snake_Head.xcor()
        Snake_Head.setx(x - 10)
    if Snake_Head.direction == 'right':
        x = Snake_Head.xcor()
        Snake_Head.setx(x + 10)


def go_up():
    Snake_Head.direction = 'up'
 

def go_down():
    Snake_Head.direction = 'down'


def go_left():
    Snake_Head.direction = 'left'


def go_right():
    Snake_Head.direction = 'right'


def Food_Collision():
    if Snake_Head.distance(
            Snake_Food) < 15:
        Snake_Food.goto(random.randint(-470, 470), random.randint(-299, 219))
        
        Snake_body = turtle.Turtle()      
        Snake_body.speed(0)
        Snake_body.shape('circle')
        Snake_body.color('red')
        Snake_body.penup()
        queue.append(Snake_body)
        return True
    return False


def Border_Collision():
#border collisions  
    if Snake_Head.xcor() > 270 or Snake_Head.xcor() < -270 or Snake_Head.ycor() > 239 or Snake_Head.ycor() < -299:
        time.sleep(1)
        Snake_Head.goto(0, 0)
        Snake_Head.direction = 'stop'
        for segment in queue:
            segment.goto(1000, 1000)
        queue.clear()
        return True

    return False
def Body_Collision():
    # body collisions
    for segment in queue:
        if segment.distance(Snake_Head) < 10:  # overlapping
            time.sleep(1)
            Snake_Head.goto(0, 0)
            Snake_Head.direction = 'stop'
            for segment in queue:
                segment.goto(1000, 1000)
            queue.clear()
            return True
    return False


def Add_Snake_Body():
    
    for i in range(len(queue) - 1, 0, -1):
        if i % 8 == 0:
            queue[i].goto(queue[i - 1].xcor(), queue[i - 1].ycor())
            queue[i].color('white')
            continue
        queue[i].goto(queue[i - 1].xcor(), queue[i - 1].ycor())
    if len(queue) > 0:
        queue[0].goto(Snake_Head.xcor(), Snake_Head.ycor())




window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')


score = 0
High_Score = 0
while True:

    window.update()
    Move_Snake()
    if Food_Collision():
        score += 10
        High_Score += 10
        if score > High_Score:
            High_Score = score
        pen.clear()
        pen.write('Score:{}    High score:{}  '.format(score, High_Score), align='center', font=('Arial', 15, 'bold'))

    if Body_Collision() or Border_Collision():
        score = 0
        pen.clear()
        pen.write('Score:{}    High score:{}  '.format(score, High_Score), align='center', font=('Arial', 15, 'bold'))
    time.sleep(delay)
    Add_Snake_Body()

window.mainloop()