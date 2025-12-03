input = open("input.txt")
dial = 50
password = 0
for rotation in input:
    sign = 0
    if rotation[0] == "R":
        sign = 1
    else:
        sign = -1
    dial += int(rotation[1:]) * sign
    if dial % 100 == 0:
        password += 1
print(password)
