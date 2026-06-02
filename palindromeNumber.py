""" # printing out in to the console
print("Hello, World")
print("This is a palindrome number checker.", "Please enter a number to check if it's a palindrome.")

# asking for input from user
Num = int(input("Check if your number is a Palindrom Number: "))
print(f"{Num} is a palidrome number.")

# functions and arguments(postional and keyword or both)
def my_function(name, age, eyeColor):
    print(f"my personal informations are; \n name: {name}, \n age: {age}, \n eyecolor: {eyeColor}")
    
my_function("peak",21, eyeColor = "brown")
 """
 
# Basic color codes
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'  # This resets the color back to default

def isPalindrome(num):
    if num == 0:
        exit
    else:    
        numCharArray = list(str(num)) 
        print(f"[debug]....{numCharArray}")
        reverseStr = ""
        for i in range(len(numCharArray)-1,-1,-1):
            reverseStr += numCharArray[i]
        
        reverseInt = int(reverseStr)
        print(f"[debug]....{reverseInt}")
        

        if num == reverseInt:
            print(f"{GREEN}{num}{RESET} is a palidrome number.")
        else:
            print(f"{RED}{num}{RESET} is not a palidrome number.") 
        
    
num = int(input("Check if your number is a Palindrome number: "))    
isPalindrome(num)
