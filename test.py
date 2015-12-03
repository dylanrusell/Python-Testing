def countDown(n):
    if(n < 0):
        return -1
    for i in range(n, -1, -1):
        print(i)
    return 0

userInput = eval(input("Enter a number: "))

errorCheck = countDown(userInput)

if(errorCheck == 0):
    print("\nSuccess!")
else:
    print("\nError!")
