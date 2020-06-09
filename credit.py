num = input(f'Number: ')

reverseNum = num[::-1]

def main():
    checkSum = 0
    for i in range(len(num)):
        digit = int(reverseNum[i])
        if i % 2 != 0:
            checkSum = checkSum + sumDigits(str(digit * 2))
        elif i % 2 == 0:
            checkSum += digit
    if checkSum % 10 == 0:
        typeCard(num)
    else:
        print("INVALID\n")

def sumDigits(n):
    sum = 0
    for i in n:
        sum += int(i)
    return(int(sum))

def typeCard(n):
    if n[0] == "4":
        print("VISA\n")
    elif n[0:2] == "34" or n[0:2] == "37":
        print("AMEX\n")
    elif n[0:2] in ["51", "52", "53", "54", "55"]:
        print("MASTERCARD\n")
    else:
        print("INVALID\n")

main()