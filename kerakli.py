import turtle as t
t.bgcolor('black')
t.tracer(50)
t.pensize(7)
t.goto(-40,-300)
c = ['green', 'pink']
t.rt(4)
for i in range(600):
    t.color(c[i%2])
    t.up()
    t.circle(300-i,-92)
    t.down()
    t.circle(300-i,-92)
t.done()