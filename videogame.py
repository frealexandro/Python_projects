import random


def run():
    f = random.randint(1, 100)
    number_choosed = int(input("input a number: "))
    while number_choosed != f:
        if number_choosed < f:
            print("choose a number  " )
        else:
            print("choose a smaller number ")
            
        number_choosed = int(input("input number : "))
    print("!win¡")     

if __name__=="__main__":
    run()
    


