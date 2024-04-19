def facto(number):
    if number == 0:
        return 1
    else:
        return number * facto(number-1)
    
number = int(input("Enter the number whose factorial you want to calculate:"))
print(f"{number}! = {facto(number)}")
print(f"{number}N = {facto(number)}")