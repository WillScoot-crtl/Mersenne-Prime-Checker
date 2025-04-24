
# Mersenne Prime
# Varify number is a prime number
# Value of mersenne prime gives probable prime

def prime_number(number):
    count = 0

    for divisor in range(2, number):
        if number % divisor != 0:
            count == 0
        else:
            count += 1
            

    if count > 0:
        return False
    else:
        return number

# After verifying number is prime, verify whether it's a mersenne prime

def check_mersenne(number):

    count = 0
    mersenne = (2 ** prime_number(number)) - 1
    
    for divisor in range(2, mersenne):
        if mersenne % divisor != 0:
            count == 0
        else:
            count += 1

    if count == 0:
        return f"{number} is a mersenne prime number. It's value is {mersenne}"
    else:
        return f"{number} is not a mersenne prime"
        

def main():
    for i in range(10):
        user_number = int(input("Enter a number: "))
    

        if prime_number(user_number) == False:
            print("Your number isn't a prime number")
        else:
            print(check_mersenne(user_number))

main()

# Lucas Lehmer (probable prime is a prime without factoring)
    
    
