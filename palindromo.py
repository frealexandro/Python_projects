def palindrome(word):
    word= word.replace(" ", "")
    word= word.lower()
    reverse_word=word[::-1]
    if word==reverse_word:
        return True
    else:
        return False


def run():
    word = input ("escribe una palabra:  " )
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("is a palindrome")
    else:
        print ("is not a palindrome") 


if __name__=="__main__":
    run()

