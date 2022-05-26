#Prime number checker

number = int(input('WHat numner would you like to check if it is prime\n'))


def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print('It is a prime number')
    else:
        print('It is not a prime number')
    

prime_checker(number=number)
