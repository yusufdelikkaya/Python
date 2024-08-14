# 2024_07_06 Yusuf Delikkaya

# Check if the inputted number is a Prime number.

def isPrime(number):

    if number <= 1:
        return False

    elif number == 2:
        return True
        
    elif number % 2 == 0:
        return False

    else:
        
        for i in range(3, int(number**0.5) + 1, 2):
            
            if number % i == 0:
                return False
            
        return True
    




number = int(input("Input a number."))

if isPrime(number) == True:
    print(f"{number} is a Prime number.")
else:
    print(f"{number} is not a Prime number.")
