# 2024_07_06 Yusuf Delikkaya

# Check if the inputted number is an Emirp number.

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
    




def isEmirp(number):

    if isPrime(number) == True:
        
        reverse_number = int(str(number)[::-1])

        if isPrime(reverse_number) == True:
            return True
        
        else:
            return False
    
    else:
        return False





number = int(input("Input a number."))

if isEmirp(number) == True:
    print(f"{number} is an Emirp number.")
else:
    print(f"{number} is not an Emirp number.")
