import turtle
import random
import time
import math


def initializeTheCells():
    for i in range(35):
        cells.append([])
        for j in range(35):
            newCell = turtle.Turtle()
            newCell.penup()
            newCell.shape("square")
            newCell.shapesize(stretch_wid = 0.9, stretch_len = 0.9)
            cells[i].append(newCell)
            newCell.state = 0
            newCell.color("gray90") #gray90 almost white
    #設定細胞的初始狀態


def selectCells(x, y):
    if x > -350 and x < 350 and y > -350 and y < 350:
        j = math.floor((x + 350)/20)
        i = math.floor((350 - y)/20)
        if onClick:
            if cells[i][j].state == 0:
                cells[i][j].state = 1
                cells[i][j].color("gray0")
                #1代表活著 --> 顏色是gray0
            else:
                cells[i][j].state = 0
                cells[i][j].color("gray90")
                #0代表死亡 --> 顏色是gray90
    wn.update()


def showTheUniverse():
    ycor = 340
    for i in range(35):
        xcor = -340
        for j in range(35):
            cells[i][j].goto(xcor, ycor)
            xcor = xcor + 20
        ycor = ycor - 20
    wn.update()




def esc():
    global stop
    stop = True

def start():
    global boundaryCondition
    global onClick

    onClick = False
    pen.clear()
    pen.write("Choose the boundary condition in the shell", font=("Verdana", 20, "normal"), align = "center")
    wn.update()
    boundaryCondition = int(input("Boundary Condition? Enter 1 for Constant or 2 for Periodic: "))
    #邊界選擇，1代表週期性邊界，2代表固定邊界
    pen.clear()
    pen.write("Press ESC to exit", font=("Verdana", 20, "normal"), align = "center")
    
    while not stop:
        wn.update()

        if boundaryCondition == 1: #恆定邊界
            next_state = [[0 for _ in range(35)] for _ in range(35)]
            #佔存，這樣才不會跑太快出錯。不能用sleep因為這只是讓畫面sleep，程式已經跑完了
            for i in range(35):
                for j in range(35):
                    byebye = 0

                    #new code(巢狀迴圈)
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy ==0:
                                continue
                            ni= i + dx
                            nj = j + dy
                            if 0 <= ni < 35 and 0 <= nj < 35:
                                if cells[ni][nj].state == 1:
                                    byebye = byebye + 1

                    if cells[i][j].state == 1:
                        if byebye < 2 or byebye >3:
                            next_state[i][j] = 0 #死
                            cells[i][j].color("gray90")
                        else:
                            next_state[i][j] = 1 #活
                            cells[i][j].color("gray0")
                    elif byebye == 3:
                        next_state[i][j] = 1 #活
                        cells[i][j].color("gray0")

        elif boundaryCondition == 2: #週期性邊界(like snake game)
            next_state = [[0 for _ in range(35)] for _ in range(35)]
            for i in range(35):
                for j in range(35):
                    byebye = 0

                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy ==0:
                                continue
                            ni = (i + dx) % 35
                            nj = (j + dy) % 35
                            if cells[ni][nj].state == 1:
                                byebye = byebye + 1

                    if cells[i][j].state == 1:
                        if byebye < 2 or byebye >3:
                            next_state[i][j] = 0 #死
                            cells[i][j].color("gray90")
                        else:
                            next_state[i][j] = 1 #活
                            cells[i][j].color("gray0")
                    elif byebye == 3:
                            next_state[i][j] = 1 #活
                            cells[i][j].color("gray0")
        time.sleep(0.05)
        
    pen.clear()
    pen.write("Done", font=("Verdana", 20, "normal"), align = "center")
    turtle.done()


 
wn = turtle.Screen()
wn.setup(width = 35*20 + 100, height = 35*20 + 100)
wn.tracer(0)

wn.listen()
wn.onkeypress(esc, "Escape") #Press ESC to exit
wn.onkeypress(start, "Return") #Press Enter to start
wn.onscreenclick(selectCells)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 365)
pen.write("Select the cells and then Press Enter to start", font=("Verdana", 20, "normal"), align = "center")

boundaryCondition = None
stop = False
onClick = True
cells = []

initializeTheCells() #Already done for you
showTheUniverse() #Already done for you

turtle.mainloop()
