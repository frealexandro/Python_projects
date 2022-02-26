def run():
    LIMIT=10000

    counter=0
    potency_2 = 2**counter
    while potency_2 < LIMIT:
        print( " 2 potency to  " + str(counter) + "is equal to  "+ str(potency_2))
        counter= counter + 1
        potency_2 = 2**counter


if __name__=="__main__":
    run() 
