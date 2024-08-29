def sum_number(num):
    sum_num = 0
    
    while num > 0:
        digit = num % 10
        sum_num = sum_num + digit
        num = num // 10
    
    return sum_num


number = int(input("Enter a number to calculate sum: "))


sum_number = sum_number(number)


print(f"The sum of number is: {sum_number}")