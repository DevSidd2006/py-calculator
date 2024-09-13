while True:  
    print("\nHi !! Welcome to Py Calculator:-")
    a = float(input("\nEnter the first number:- "))

    print("1. Addition ")
    print("2. Difference ")
    print("3. Multiply ")
    print("4. Divide ")
    print("5. Power ")

    w = int(input("\nEnter Choice Code :- (1/2/3/4/5): "))
    
    if w == 1:
        print("\nYou chose Addition.")
    elif w == 2:
        print("\nYou chose Substraction.")
    elif w == 3:
        print("\nYou chose Multiplication.")
    elif w == 4:
        print("\nYou chose Division.")  
    elif w == 5:
        print("\nYou chose Power.")
    else:
        print("\nEnter a valid input , and try Again.")
        break

    b = float(input("\nEnter the second number:- "))

    sum = a + b
    dif = a - b
    mul = a * b
    div = a / b
    pow = a ** b

    if w == 1:
        print("\nAddition = ", sum)
    elif w == 2:
        print("\nDifference = ", dif)
    elif w == 3:
        print("\nMultiplication = ", mul)
    elif w == 4:
        if b == 0:
            print("\nNot Defined (Cannot divide by Zero)")
        else:
            print("\nDivision = ", div)
    elif w == 5:
        print("\nPower = ", pow)
    else:
        print("Enter a valid input.")
        break

    print("\nDo you want to perform another operation? (1. Yes or 2. No)")
    next = input("\nEnter a choice code:- ").lower()

    if next == '1' or next == 'yes':
        print("\nOk! Let's start it again.")
        continue  
    elif next == '2' or next == 'no':
        print("\nGoodbye!")
        break  