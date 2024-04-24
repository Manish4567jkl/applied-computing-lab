def isPalindrome(x):
    if x < 0:
        return False

    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    return reversed_num == x

print(isPalindrome(121))  

