import turtle

turtle.shape('turtle')
turtle.penup()

while True :
    x = int(input("X : "))
    y = int(input("Y : "))
    text = input("String : ")
    
    turtle.goto(x, y)
    turtle.write(text, font=("Arial", 30))
    
turtle.done()