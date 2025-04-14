import turtle
import random
import time
import math

global i
global j

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

        ###### YOUR CODE #####
        # For a cell at row i and column j find the sum of the neighbors' cell
        # values by considering the boundary condition
        # Update each cell to alive/dead based on the rules. 

        if boundaryCondition == 1:
            #如果周圍三個都是死的(0),那中間那個就是死的
            #if byebye == 3 --> center is dead

            if cells[i][j].state == 1: #中間活
                byebye = 0

                if cells[i-1][j].state == 1: #上面
                    byebye = byebye + 1
                if cells[i][j-1].state == 1: #左邊
                    byebye = byebye + 1
                if cells[i][j+1].state == 1: #右邊
                    byebye = byebye + 1
                if cells[i+1][j].state == 1: #下面
                    byebye = byebye + 1
                if cells[i-1][j-1].state == 1: #左上
                    byebye = byebye + 1
                if cells[i-1][j+1].state == 1: #右上
                    byebye = byebye + 1
                if cells[i+1][j-1].state == 1: #左下
                    byebye = byebye + 1
                if cells[i+1][j+1].state == 1: #右下
                    byebye = byebye + 1

                if byebye < 2 or byebye > 3:
                    cells[i][j].state = 0
                    cells[i][j].color("gray90") #死
                elif byebye == 2 or byebye == 3:
                    cells[i][j].state = 1
                    cells[i][j].color("gray0") #活

            elif cells[i][j].state == 0: #中間死
                byebye = 0

                if cells[i-1][j].state == 1: #上面
                    byebye = byebye + 1
                if cells[i][j-1].state == 1: #左邊
                    byebye = byebye + 1
                if cells[i][j+1].state == 1: #右邊
                    byebye = byebye + 1
                if cells[i+1][j].state == 1: #下面
                    byebye = byebye + 1
                if cells[i-1][j-1].state == 1: #左上
                    byebye = byebye + 1
                if cells[i-1][j+1].state == 1: #右上
                    byebye = byebye + 1
                if cells[i+1][j-1].state == 1: #左下
                    byebye = byebye + 1
                if cells[i+1][j+1].state == 1: #右下
                    byebye = byebye + 1

                if byebye == 3:
                    cells[i][j].state = 1
                    cells[i][j].color("gray0") #活


        elif boundaryCondition == 2:
            
        else:
            print("Pls enter 1 or 2 and try again.")
            boundaryCondition = int(input("Boundary Condition? Enter 1 for Constant or 2 for Periodic: "))


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
