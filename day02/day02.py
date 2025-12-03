import sys

input = open(sys.argv[1])
ranges = input.read().split(",")
invalidIDSum = 0
for range in ranges:
    splitRange = range.split("-")
    min = int(splitRange[0])
    max = int(splitRange[1])

    while min <= max:
        minLen = len(str(min))
        if minLen % 2 == 1:
            min = 10**minLen
            continue

        # e.g., if min is 123456, divide by 1000 and discard remainder
        divisor = 10 ** round(minLen / 2)
        minLeft = int(min / divisor)

        # create an invalid ID from minLeft, and see if it's in range
        guess = minLeft * divisor + minLeft
        if (guess >= min) and (guess <= max):
            invalidIDSum += guess

        # increment minLeft and pad with zeros
        min = minLeft * divisor + divisor

print(invalidIDSum)
