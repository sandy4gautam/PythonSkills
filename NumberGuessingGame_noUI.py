import random
def guess():
    n = random.randint(1,100)
    count = 0;
    while True:
        count+=1
        try:
            user_input = int(input('Enter a number: '))
        except ValueError:
            print('Only Enter numbers')
        if n == user_input:
            print(f'Bravo!! You guessed it in {count} tries.')
            input2 = input('Do you want to play again? (y or n): ').lower()
            if(input2 == 'n'):
                break
            elif(input2 == 'y'):
                guess()
            else:
                print('only enter either y or n.')
        elif 5 < (abs(n-user_input)) <= 10:
            print('Hey! you are close!')
        elif (abs(n-user_input)) <5:
            print('Almost There!! veryy close!')
        elif (abs(n-user_input)) >10 :
            print('Common!!! you can do better. Try again!!')

guess()
