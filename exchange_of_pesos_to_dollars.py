def exchange(value_dolar,type_pesos):
    pesos = input ("¿how many" + type_pesos +"do you have?:  ")
    pesos = float(pesos)
    dolar  = pesos/value_dolar
    dolar = round (dolar,2)
    dolar = str(dolar)
    print (" you have $ " + dolar + " american dolars ")



menu = """ 
welcome to the exchange🎖🎖🎖
1 - colombian pesos 
2 - argentin pesos 
3 - chilenian pesos 
Choose a option:  """
option=int(input(menu))
if option == 1:
    converter(3875,"colombian")
elif option == 2:
    converter(65,"argentin")
elif option == 3:
    converter(24,"chilenian")
else:
    print("choose a correct option please ")







