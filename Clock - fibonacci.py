#Fibonacci clock by balegastate
#How to read the clock:
#1. Sum the value of red and blue squares ----> hours
#2. Sum the value of green and blue squares and multiply by 5 ----> minutes

import time
import turtle
import random

#Finds all fibonacci sums of a number
def find_sums(num, m, s):
    global final, fib
    if m == -1:
        final = []
    for i in range(m+1, 5):
        if fib[i] < num:
            find_sums(num - fib[i], i, s + str(i))
        elif fib[i] == num:
            final.append(s + str(i))

#Draws individual rectangles of the clock
def draw_rect(pen, x, y, side, color):
    pen.up()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(side)
        pen.right(90)
    pen.end_fill()

def draw_clock(pen, colors):
    palette = ["white", "red", "green", "blue"]
    x = [-100, -400, -400, -200, -200]
    y = [ 250,   50,  250,  150,  250]
    w = [ 500,  300,  200,  100,  100]
    for i in range(5):
        draw_rect(pen, x[i], y[i], w[i], palette[colors[i]])

#Turtle setup
window = turtle.Screen()
window.bgcolor("black")
window.setup(width=800, height=500)
window.title("Fibonacci Clock")
window.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

fib = [5, 3, 2, 1, 1]
final = []
h_bef = -1
m_bef = -1

while True:
    #Get time and convert it
    h_time = int(time.strftime("%I"))
    m_time = int(time.strftime("%M"))
    h = h_time
    m = round((m_time - (m_time // 5) * 5) / 5) + (m_time // 5)
    if m == 12:
        m = 0
        h += 1

    #Update colors for each fibonacci square
    if h != h_bef or m != m_bef:
        find_sums(h, -1, "")
        h_str = str(final[random.randint(0, len(final) - 1)])
        find_sums(m, -1, "")
        if final:
            m_str = str(final[random.randint(0, len(final) - 1)])
        else:
            m_str = ""

        colors = [0, 0, 0, 0, 0]
        for i in h_str:
            colors[int(i)] += 1
        for i in m_str:
            colors[int(i)] += 2

    #Draw the clock
    draw_clock(pen, colors)
    window.update()

    time.sleep(1)
    pen.clear()

    h_bef = h
    m_bef = m

window.mainloop()