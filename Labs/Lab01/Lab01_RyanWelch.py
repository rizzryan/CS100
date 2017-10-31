# Ryan Welch
# CS100 2017F Section 105
# Lab01, Oct 19, 2017
def palindrome(aStr):
    aStr = aStr.replace(' ', '')
    if aStr[0:] == aStr[::-1]:
        return('\'{}\' is a palindrome.'.format(aStr))
    else:
        return('\'{}\' is not a palindrome.'.format(aStr))

def luhn(num):
    num = int(num)
    numList = []
    digit2Times = []
    doubleDigit = []
    sum = 0
    totalSum = 0
    
    for digits in str(num):
        numList.append(digits)

    for elems in range(len(numList)):
        if elems % 2 != 0:
            digit2Times.append(int(numList[elems]) * 2)
    
    for doubleDigits in digit2Times:
        if len(str(doubleDigits)) % 2 == 0:
            try:
                doubleDigit.append(doubleDigits)
            except:
                return('Invalid number!')
            doubleDigit = str(doubleDigit)
            sum += int(doubleDigit[1]) + int(doubleDigit[2])
        else:
            sum += int(doubleDigits)

    for elems in range(len(numList)):
        if elems % 2 == 0:
            sum += int(numList[elems])
    sum = str(sum)
    if int(sum[-1]) % 2 == 0:
        return('Valid number!')
    else:
        return('Invalid number!')
    
def greedy(changeAmount):
    changeAmount = int(float(changeAmount) * 100)
    coinList = [25, 10, 5, 1]
    newCoinList = []
    
    for coins in coinList:
        totalCoinCount = changeAmount // coins
        newCoinList += [coins] * totalCoinCount
        changeAmount -= coins * totalCoinCount
    
    print('You need {} coins.'.format(len(newCoinList)))

if __name__ == '__main__':
    while True:
        word = input('Give me a word: ')
        if len(word) > 0:
            print(palindrome(word))
        else:
            break

    masterVals = ['51', '52', '53', '54', '55']
    
    while True:
        num = input('Enter in a credit/debit card number: ')
        if len(num) == 0:
            break
        else:
            if num[0] == '4':
                print('VISA')

            if num[0:2] == '34' or str(num)[0:2] == '37':
                print('AMEX')

            if num[0:2] in masterVals:
                print('MASTERCARD')

            if len(num) > 0:
                print(luhn(num))
            else:
                break
    while True:
        amount = input('Enter in the change owed in the format XX.XX: ')
        if amount > '0':
            greedy(amount)
        elif len(str(amount)) == 0:
            break
