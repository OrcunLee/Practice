print('Welcome to the top calculator!')
bill = float(input('What was the total bill? ($) : '))
tip = int(input('How much tip would pu like to give? 10, 12 or 15? : '))
people = int(input('How many people to split the bill? : '))
bill_tip = tip/100 * bill + bill/people
print(f'Each person should pay : ${round(bill_tip, 2)}')