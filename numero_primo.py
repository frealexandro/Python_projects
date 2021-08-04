def es_primo(numero):
    contador= 0
    for i in range (1,numero+1):
        if i == numero or  i ==1:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False    






def run():
    numero=int(input("escribe un numero: "))
    if es_primo (numero):
        print("el numero es primo")
    else:
        print("el numero no es primo")


if __name__== "__main__":
    run()