# Estrella

Dirección GitHub de este repositorio: https://github.com/carlospuigserver/Estrella.git

Para realizar este programa he tenido que ser capaz de adaptarme al entorno de turtle, llevando a cabo una función, con unas ciertas condiciones y finalmente un bucle,para poder ser capaz de crear una condición para crear un una estrella a partir de las puntas que eligas.

El diagrama de flujo de este repositorio:
<img width="730" alt="estrella" src="https://user-images.githubusercontent.com/91721643/146836975-b08730c2-7b2f-46f3-a321-181cee5b18c8.png">


El link del figma por si no se ve correctamente la imagen es:
https://www.figma.com/file/xksWyRqrdqcrx10Xb0X7T8/Untitled?node-id=0%3A1










El códigop que he empleado para realizar este repositorio es 
```import turtle

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

if __name__=='__main__':
    n=int(input("Determina las puntas de la estrella:   "))
    estrella(n)          



