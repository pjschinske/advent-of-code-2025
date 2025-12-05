import sys
import numpy as np

# load grid into memory, in this case a numpy grid
input = open(sys.argv[1])
grid = None
gridCount = None
rowLength = 0
rowIndex = 0
for row in input:
    if grid is None:
        rowLength = len(row) - 1
        grid = np.empty((rowLength, rowLength), dtype=np.int32)
        gridCount = np.zeros((rowLength, rowLength), dtype=np.int32)
    for i in range(0, rowLength):
        match row[i]:
            case ".":
                grid[rowIndex, i] = 0
            case "@":
                grid[rowIndex, i] = 1
    rowIndex += 1

# now we basically do the jpeg algorithm


def countRollsTopRow(grid, gridCount, rowLength):
    gridCount[0, 0] = grid[0, 1]
    gridCount[0, 0] += grid[1, 0]
    gridCount[0, 0] += grid[1, 1]
    for i in range(1, rowLength - 1):
        gridCount[0, i] = grid[0, i - 1]
        gridCount[0, i] += grid[0, i + 1]
        gridCount[0, i] += grid[1, i - 1]
        gridCount[0, i] += grid[1, i]
        gridCount[0, i] += grid[1, i + 1]
    gridCount[0, rowLength - 1] = grid[0, rowLength - 2]
    gridCount[0, rowLength - 1] += grid[1, rowLength - 2]
    gridCount[0, rowLength - 1] += grid[1, rowLength - 1]


# TODO: add row above (since I just copied the top row code),
# then make countRollsBottomRow(...)
def countRollsMiddleRow(grid, gridCount, rowLength, row):
    gridCount[row, 0] = grid[row - 1, 0]
    gridCount[row, 0] += grid[row - 1, 1]
    gridCount[row, 0] += grid[row, 1]
    gridCount[row, 0] += grid[row + 1, 0]
    gridCount[row, 0] += grid[row + 1, 1]
    for i in range(1, rowLength - 1):
        gridCount[row, i] = grid[row - 1, i - 1]
        gridCount[row, i] += grid[row - 1, i]
        gridCount[row, i] += grid[row - 1, i + 1]
        gridCount[row, i] += grid[row, i - 1]
        gridCount[row, i] += grid[row, i + 1]
        gridCount[row, i] += grid[row + 1, i - 1]
        gridCount[row, i] += grid[row + 1, i]
        gridCount[row, i] += grid[row + 1, i + 1]
    gridCount[row, rowLength - 1] = grid[row - 1, rowLength - 2]
    gridCount[row, rowLength - 1] += grid[row - 1, rowLength - 1]
    gridCount[row, rowLength - 1] += grid[row, rowLength - 2]
    gridCount[row, rowLength - 1] += grid[row + 1, rowLength - 2]
    gridCount[row, rowLength - 1] += grid[row + 1, rowLength - 1]


def countRollsBottomRow(grid, gridCount, rowLength):
    lastRow = rowLength - 1
    gridCount[lastRow, 0] = grid[lastRow - 1, 0]
    gridCount[lastRow, 0] += grid[lastRow - 1, 1]
    gridCount[lastRow, 0] += grid[lastRow, 1]
    for i in range(1, rowLength - 1):
        gridCount[lastRow, i] = grid[lastRow - 1, i - 1]
        gridCount[lastRow, i] += grid[lastRow - 1, i]
        gridCount[lastRow, i] += grid[lastRow - 1, i + 1]
        gridCount[lastRow, i] += grid[lastRow, i - 1]
        gridCount[lastRow, i] += grid[lastRow, i + 1]
    gridCount[lastRow, rowLength - 1] = grid[lastRow - 1, rowLength - 2]
    gridCount[lastRow, rowLength - 1] += grid[lastRow - 1, rowLength - 1]
    gridCount[lastRow, rowLength - 1] += grid[lastRow, rowLength - 2]


totalSum = 0
sum = 1
while sum != 0:
    countRollsTopRow(grid, gridCount, rowLength)
    for i in range(1, rowLength - 1):
        countRollsMiddleRow(grid, gridCount, rowLength, i)
    countRollsBottomRow(grid, gridCount, rowLength)

    print(gridCount)
    sum = 0
    for r in range(0, rowLength):
        for c in range(0, rowLength):
            if grid[r, c] == 1 and gridCount[r, c] < 4:
                sum += 1
                grid[r, c] = 0
    print(sum)
    totalSum += sum

print("total sum: " + str(totalSum))
