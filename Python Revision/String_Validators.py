if __name__ == '__main__':
    s = input()
    alphanum = False 
    alphabetical = False 
    number = False 
    lowercase = False 
    Uppercase = False
    
    for i in s:
        if alphanum == False:
            if(i.isalnum()):
                alphanum = True

        if alphabetical == False:
            if(i.isalpha()):
                alphabetical = True

        if number == False:
            if(i.isdigit()):
                number = True

        if lowercase == False:
            if(i.islower()):
                lowercase = True

        if Uppercase == False:
            if(i.isupper()):
                Uppercase = True

    print(f"{alphanum}\n{alphabetical}\n{number}\n{lowercase}\n{Uppercase}")