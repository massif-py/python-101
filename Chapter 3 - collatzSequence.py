def collatz(number):
    evenNumber = 0
    oddNumber = 0
    while True:
        if number == 1: #Final step.
            print('Odd number', number)
            oddNumber = oddNumber + 1
            break
        elif(number % 2) == 0: #Even number.
            print('Even number', number)
            number = (number // 2)
            evenNumber = evenNumber + 1
        elif (number % 2) == 1: #Odd number.
            print('Odd number', number)
            number = (3 * number + 1)
            oddNumber = oddNumber + 1
        else: #Error case.
            print('ERROR.')

    totalAmount = evenNumber + oddNumber
    print('Total amount of even numbers:', evenNumber, 'Percentage of even numbers:', evenNumber/totalAmount)
    print('Total amount of odd numbers:', oddNumber, 'Percentage of odd numbers:', oddNumber/totalAmount)
    print('Total amount of numbers:', totalAmount)
        
while True:
    try:
        print('Type a number.')
        intNumber = int(input())
        break
    except ValueError:
        print('You must enter an integer number.')

collatz(intNumber)

        
    
