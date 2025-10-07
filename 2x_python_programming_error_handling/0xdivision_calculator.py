try:
    
    divisor = int (input("Enter the Numerator: "))
    dividend = int (input("Enter the Denominator: "))

    Answer = divisor/dividend
    
    print (f"{divisor} is the divisor and {dividend} is the dividend")

    print (Answer)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")