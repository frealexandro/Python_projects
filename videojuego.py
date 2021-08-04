import random


def run():
    f = random.randint(1, 100)
    numero_elegido = int(input("ingresa un numero: "))
    while numero_elegido != f:
        if numero_elegido < f:
            print("elige un numero mas grande" )
        else:
            print("elige un numero mas pequeño")
            
        numero_elegido = int(input("ingresa un numero: "))
    print("!ganaste¡")     

if __name__=="__main__":
    run()
    


