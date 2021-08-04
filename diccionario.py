def run():
    # mi_diccionario = {
    #     'llave 1': 25,
    #     'llave 2': 26,
    #     'llave 3': 27,
    # }
    # print(mi_diccionario['llave 1'])
    # print(mi_diccionario['llave 2'])
    # print(mi_diccionario['llave 3'])
    
    
    poblacion_paises={
        'bogota': 20000,
        'cali':5000,
        'boyaca':400,
    }
    # print(poblacion_paises['cali'])

    # for pais in poblacion_paises.keys():
    #     print(pais)
    # for pais in poblacion_paises.values():
    #     print(pais)
    for pais,poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes' )





if __name__=='__main__':
    run()