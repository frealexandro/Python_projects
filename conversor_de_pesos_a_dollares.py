def conversor(valor_dolar,tipo_pesos):
    pesos = input ("¿cuantos pesos" + tipo_pesos +"tienes?:  ")
    pesos = float(pesos)
    dolar  = pesos/valor_dolar
    dolar = round (dolar,2)
    dolar = str(dolar)
    print (" tienes $ " + dolar + " dolares americanos ")



menu = """ 
bienvenido al conversor de monedas🎖🎖🎖
1 - pesos colombianos 
2 - pesos argentinos 
3 - pesos chilenos 
Elige una opcion:  """
opcion=int(input(menu))
if opcion == 1:
    conversor(3875,"colombianos")
elif opcion == 2:
    conversor(65,"argentinos")
elif opcion == 3:
    conversor(24,"colombianos")
else:
    print("elije una opcion correcta porfavor ")







