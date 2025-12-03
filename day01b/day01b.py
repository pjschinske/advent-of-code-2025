input = open("test.txt")
dial = 50
password = 0
for instruction in input:
    sign = 0
    if instruction[0] == "R":
        sign = 1
    else:
        sign = -1
    rotation = int(instruction[1:]) * sign

    wasPositive = dial > 0
    wasNegative = dial < 0
    dial += rotation
    isNotNegative = dial >= 0
    isNotPositive = dial <= 0
    # edge case: magnitude won't change if we go from -5 to 5, but we will need
    # to increment password
    # This also implements the "lands on 0" case
    if (wasNegative and isNotNegative) or (wasPositive and isNotPositive):
        password += 1
    magnitude = int(dial / 100)
    password += abs(magnitude)
    dial -= magnitude * 100  # get dial to within [-99, 99]
print(password)
