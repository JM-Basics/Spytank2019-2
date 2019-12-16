import spytank

z ="z : avancer" 
s ="s : reculer"
q ="q : tourner à gauche"
d ="d : tourner à droite"
vp ="a : plus vite" 
vm ="e : moins vite"
x ="x : stop"
vitesse = 150

print(z,s,q,d,vp,vm,x)

while True:
    lettre = input(">>> ")
    if lettre == "z" : 
        spytank.avance(vitesse)
    elif lettre == "s" :
        spytank.recule(vitesse)
    elif lettre == "q" :
        spytank.gauche(vitesse)
    elif lettre == "d" : 
        spytank.droite(vitesse)
    elif lettre == "a" :
        if vitesse < 250 :
            vitesse = vitesse + 20
    elif lettre == "e" :
        if vitesse > 70 : 
            vitesse = vitesse -20
    elif lettre == "x" :   
        spytank.stop()
    