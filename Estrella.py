import turtle

# Defino función estrella
def estrella(n):
    def angulo():
        angulo=0        # Defino condiciones para las puntas de las estrellas
        if n%3==0:
            angulo=(360/n)+120
        elif n%4 ==0:
            angulo=180-(360/n)
        else:
            return angulo
    turtle.speed(0)
    for _ in range(n):
        turtle.right(angulo()) # Bucle para crear la figura
        turtle.forward(200)
    turtle.done()



