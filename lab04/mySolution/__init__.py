import turtle
import random

def tree(branchLen,t,size = 8):
    rand2 = random.randint(15, 22)
    # if branchLen <= 5 it will change pensize to make the ends thinner and make the ends green
    if branchLen<=5:
        t.pensize(1)
        t.color("green")
    # if branchLen>5 the size will decrease every time by half so the branches get thinner towards the ends
    if branchLen > 5:
        t.forward(branchLen)
        t.right(rand2)
        t.pensize(size)
        tree(branchLen-random.randint(8,17),t, size/2)
        t.left(rand2*2)
        t.pensize(size)
        tree(branchLen-random.randint(8,17),t, size/2)
        t.right(rand2)
        t.backward(branchLen)
        t.color("brown")
        
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.pensize(8)
    t.color("brown")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed("fastest")
    tree(75, t)
    myWin.exitonclick()

#main()

def power(x, n, acc = 1):
    if n == 0:
        return acc
    else:
        return power(x, n-1, acc*x)

def powerH(x, n):
    if n == 0:
        return 1
    elif n%2 == 1:
        return powerH(x, n//2) * powerH(x, n//2) * x
    else:
        return powerH(x, n//2) * powerH(x, n//2)


def binomial(n, k):
    if k == n or k == 0:
        return 1
    else:
        return binomial(n-1, k) + binomial(n-1, k-1)
