import network
import click 

IP = "10.0.0.121"
PORT = 1111

z ="z : avancer" 
s ="s : reculer"
q ="q : tourner à gauche"
d ="d : tourner à droite"
vp ="+ : plus vite" 
vm ="- : moins vite"
x ="x : stop"
a = "a : allumer ou eteindre les leds"
vitesse = 150
continuer = True
direction = 1

# 1 pour avancer ; 2 pour reculer; 3 gauche;4 droite
print(z,s,q,d,vp,vm,x)

while True:
    socket = network.newClientSocket()
    socket.connect((IP,PORT))

    print("Tape la lettre a afficher")
    lettre = click.getchar()

    socket.send(lettre.encode())
    #Byte = Octet
    #bit = 0 et 1


