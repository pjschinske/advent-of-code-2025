import sys

input = open(sys.argv[1])
sum = 0
for bank in input:
    biggestIndex = 0
    biggest = 0
    secondBiggestIndex = 0
    secondBiggest = 0
    # first, we find the biggest number that isn't the last number.
    # this will be the first cell
    # the "- 2" is to ignore the /n at the end, and the last number
    for i in range(0, len(bank) - 2):
        cellJoltage = int(bank[i])

        if cellJoltage > biggest:
            biggestIndex = i
            biggest = cellJoltage

    # then, we find the next biggest number after the number we just found.
    # this will be the second cell
    for i in range(biggestIndex + 1, len(bank) - 1):
        cellJoltage = int(bank[i])

        if cellJoltage > secondBiggest:
            secondBiggestIndex = i
            secondBiggest = cellJoltage

    # print(str(biggest) + " " + str(secondBiggest))
    sum += biggest * 10 + secondBiggest
print(sum)
