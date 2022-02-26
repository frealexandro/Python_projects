def is_prime(number):
    counter= 0
    for i in range (1,number+1):
        if i == number or  i ==1:
            continue
        if number % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False    






def run():
    number=int(input("input a number: "))
    if is_prime (number):
        print("is a prime number")
    else:
        print("is not a prime number")


if __name__== "__main__":
    run()
