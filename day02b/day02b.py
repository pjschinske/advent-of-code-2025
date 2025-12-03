import sys

input = open(sys.argv[1])
idRanges = input.read().split(",")
invalidIDSum = 0
for idRange in idRanges:
    splitRange = idRange.split("-")
    minID = int(splitRange[0])
    maxID = int(splitRange[1])

    # while min <= max:
    #     minLen = len(str(min))
    #     if minLen % 2 == 1:
    #         min = 10**minLen
    #         continue

    #     # e.g., if min is 123456, divide by 1000 and discard remainder
    #     divisor = 10 ** round(minLen / 2)
    #     minLeft = int(min / divisor)

    #     # create an invalid ID from minLeft, and see if it's in range
    #     guess = minLeft * divisor + minLeft
    #     if (guess >= min) and (guess <= max):
    #         invalidIDSum += guess

    #     # increment minLeft and pad with zeros
    #     min = minLeft * divisor + divisor

    # for each id, check if it's one character repeated, or two, three, etc
    for ID in range(minID, maxID + 1):
        idStr = str(ID)
        idLen = len(idStr)
        if idLen == 1:
            continue
        foundInvalidID = True
        for sequenceLen in range(1, int(idLen / 2) + 1):
            # if ID length isn't a multiple of the sequence length,
            # then the sequence can't fit into the ID right
            if idLen % sequenceLen != 0:
                continue

            # sequence is first n characters of id
            sequence = idStr[:sequenceLen]
            # loop through id and see if the sequence is there
            # if not, go to the next id
            foundInvalidID = True
            for i in range(sequenceLen, idLen, sequenceLen):
                if idStr[i : i + sequenceLen] != sequence:
                    foundInvalidID = False
                    break
            if foundInvalidID:
                break
        if foundInvalidID:
            print(ID)
            invalidIDSum += ID

print("Sum of invalid IDs: " + str(invalidIDSum))
