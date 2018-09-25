from itertools import count
from collections import namedtuple
from math import ceil, floor, log10, sqrt

Step  = namedtuple("Step", ["dx", "dy"])
RIGHT = Step( 1,  0)
DOWN  = Step( 0,  1)
LEFT  = Step(-1,  0)
UP    = Step( 0, -1)

def spiral():
    for n in count(start=1):
        if n % 2:
            yield RIGHT
            for i in range(n):
                yield UP
            for i in range(n):
                yield LEFT
        else:
            yield LEFT
            for i in range(n):
                yield DOWN
            for i in range(n):
                yield RIGHT

def draw_spiral(max_num):

    if(max_num < 0):
        print("NEGATIVE NUMBER NOT ALLOWED -> ONLY POSITIVE NATURAL NUMBER ALLOWED")
    elif(max_num == 0):
        print("PLEASE ENTER ONLY POSITIVE NATURAL NUMBER")
    else:
        print("\t*********** This is your desired spiral matrix **********")
        max_n = int(ceil(sqrt(max_num)))+1

        max_num_width = int(floor(log10(max_num))) + 1

        def output(item, format_string="{{:>{}}}".format(max_num_width)):
            return format_string.format(item)
    
        EMPTY = output("")
        square = [[EMPTY] * max_n for _ in range(max_n)]

        x = y = max_n // 2
        square[y][x] = output(1)

        for i, step in enumerate(spiral(), start=2):
            if i > max_num:
                break
            else:
                x += step.dx
                y += step.dy
                square[y][x] = output(i)

        print("\n".join(" ".join(row) for row in square))


number = int(input("Enter an number : "))
draw_spiral(number)
