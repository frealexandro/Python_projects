import random
def generator_keyword():
    capital_letter=['A','B','C','D','E','F','G','H','I']
    letter=['j','k','l','m','n','o','p','f','s','e','r']
    symbols=['!','$','%','&']
    numbers=['1','2','3','4','5','6']

    caracters = capital_letter+letter+symbols+numbers

    keyword= []
    for i in range(15):
        caracter_random=random.choice(caracters)
        keyword.append(caracter_random)

    keyword = "".join(keyword)
    return keyword




def run():
    keyword = generator_keyword()
    print('your new keyword is ' + keyword)


if __name__=='__main__':
    run()