import math

principal_Amount = int(input("Enter your principal amount:  "))

Annual_rate = int(input("Enter your annual intrest rate:  "))

number_of_Years = int(input("Enter the duration in year:  "))

No_Of_Year = 12 * number_of_Years

rate = Annual_rate / 100

Monthly_Rate = rate / 12 

month_base = 1 + Monthly_Rate

base = month_base ** No_Of_Year

first_number = principal_Amount * Monthly_Rate
num2 = base - 1

Monthly_payment = first_number * base / num2

print(f'{Monthly_payment:,.2f}')