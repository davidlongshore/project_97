attempts = 2

print("attempts total: " + str(attempts))

print("chose a number between 1-5")
pocketMoney=int( input('enter a number: '))

if(pocketMoney == 5):
    print('number is correct. you win.')

if(pocketMoney < 5):
    print('you aint got it')
    attempts = attempts - 1
    print('attempts left: ' + str(attempts))
    pocketMoney=int( input('enter a number: '))

if(attempts == 0):
    print("you lost. number is:" + str(number))