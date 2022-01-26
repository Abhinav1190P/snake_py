import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()

w = curses.newwin(sh,sw,0,0)

w.keypad(1)
w.timeout(100)
sx = sw/4
sy = sh/2


snake = [
    [sy,sx],
    [sy,sx-1],
    [sy,sx-2]
]

points = 0
titleCor = [0,10]

pointsCor = [0,sh-1]



key = curses.KEY_RIGHT

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_S1)

while True:
    next_key = w.getch()
    if next_key == -1:
        pass
    else:
        key = next_key


    newHead = [snake[0][0],snake[0][1]]

    if key == curses.KEY_UP:
        newHead[0] = newHead[0] - 1
    elif key == curses.KEY_DOWN:
        newHead[0] = newHead[0] + 1
    elif key == curses.KEY_LEFT:
        newHead[1] = newHead[1] - 1
    elif key == curses.KEY_RIGHT:
        newHead[1] = newHead[1] + 1

    snake.insert(0,newHead)

    if snake[0] == food:
        points = points + 5
        food = None
        while food is None:
            newFood = [
                random.randint(1,sh-1),
                random.randint(1,sw-1)
            ]
            if newFood not in snake:
                food = newFood
                w.addch(food[0],food[1],curses.ACS_S1)
            else:
                food = None
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), " ")


    w.addch(int(snake[0][0]),int(snake[0][1]), "+")

    w.addstr(int(titleCor[0]),int(titleCor[1]),"Score")
    w.addstr(int(pointsCor[0]),int(pointsCor[1]),str(points))


    if snake[0][0] == 0 or snake[0][1] == 0 or snake[0][0] == sh or snake[0][1] == sw or snake[0] in snake[1:]:
        curses.endwin()
        quit()

