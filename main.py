num = int(input("Enter the number: "))
temp = num
result = 0

while temp > 0:
    digit = temp % 10
    result = (result * 10) + digit
    temp = temp // 10

if num == result:
    print(num, "is a Palindrome number")
else:
    print(num, "is not a Palidrome number")