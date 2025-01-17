def count_digits(num):
    num = abs(num)
    if num == 0:
        return 1  # 0 has 1 digit
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

number = int(input("Enter an integer: "))
digit_count = count_digits(number)
print(f"The number of digits in {number} is: {digit_count}")