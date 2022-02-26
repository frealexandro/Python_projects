def run():
    # my_dictionary = {
    #     'key 1': 25,
    #     'key 2': 26,
    #     'key 3': 27,
    # }
    # print(my_dictionary['key 1'])
    # print(my_dictionary['key 2'])
    # print(my_dictionary['key 3'])
    
    
    country_population={
        'bogota': 20000,
        'cali':5000,
        'boyaca':400,
    }
    # print(country_population['cali'])

    # for country in country_population.keys():
    #     print(country)
    # for country in country_population.values():
    #     print(country)
    for country,population in country_population.items():
        print(country + ' have ' + str(population) + ' habitants' )





if __name__=='__main__':
    run()
