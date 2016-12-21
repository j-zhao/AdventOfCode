"""
http://adventofcode.com/2016/day/1
"""

class Day1:
    def solutionPart1(input):
        xcor = 0
        ycor = 0
        directions = ["N", "E", "S", "W"]
        currDir = 0
        for x in input:
            if x[0] == "R":
                currDir = (currDir + 1) % 4
            else:
                currDir = (currDir - 1) % 4
#            print("You are currently facing: " + directions[currDir])
            distance = int(x[1:])
            if directions[currDir] == "N":
                ycor += distance
            elif directions[currDir] == "E":
                xcor += distance
            elif directions[currDir] == "S":
                ycor -= distance
            elif directions[currDir] == "W":
                xcor -= distance
#            print("You are at: " + str(xcor) + ", " + str(ycor))
        return abs(xcor) + abs(ycor)
    def solutionPart2(input):
        xcor = 0
        ycor = 0
        directions = ["N", "E", "S", "W"]
        currDir = 0
        visited = []
        for x in input:
            if x[0] == "R":
                currDir = (currDir + 1) % 4
            else:
                currDir = (currDir - 1) % 4
            distance = int(x[1:])
            if directions[currDir] == "N":
                for i in range(0, distance):
                    ycor += 1
                    currCoor = [xcor, ycor]
                    if currCoor in visited:
                        return abs(xcor) + abs(ycor)
                    else:
                        visited.append(currCoor)
            elif directions[currDir] == "E":
                for i in range(0, distance):
                    xcor += 1
                    currCoor = [xcor, ycor]
                    if currCoor in visited:
                        return abs(xcor) + abs(ycor)
                    else:
                        visited.append(currCoor)
            elif directions[currDir] == "S":
                for i in range(0, distance):
                    ycor -= 1
                    currCoor = [xcor, ycor]
                    if currCoor in visited:
                        return abs(xcor) + abs(ycor)
                    else:
                        visited.append(currCoor)
            elif directions[currDir] == "W":
                for i in range(0, distance):
                    xcor -= 1
                    currCoor = [xcor, ycor]
                    if currCoor in visited:
                        return abs(xcor) + abs(ycor)
                    else:
                        visited.append(currCoor)

# Run with input
input = ["R1", "L4", "L5", "L5", "R2", "R2", "L1", "L1", "R2", "L3", "R4", "R3", "R2", "L4", "L2", "R5", "L1", "R5", "L5", "L2", "L3", "L1", "R1", "R4", "R5", "L3", "R2", "L4", "L5", "R1", "R2", "L3", "R3", "L3", "L1", "L2", "R5", "R4", "R5", "L5", "R1", "L190", "L3", "L3", "R3", "R4", "R47", "L3", "R5", "R79", "R5", "R3", "R1", "L4", "L3", "L2", "R194", "L2", "R1", "L2", "L2", "R4", "L5", "L5", "R1", "R1", "L1", "L3", "L2", "R5", "L3", "L3", "R4", "R1", "R5", "L4", "R3", "R1", "L1", "L2", "R4", "R1", "L2", "R4", "R4", "L5", "R3", "L5", "L3", "R1", "R1", "L3", "L1", "L1", "L3", "L4", "L1", "L2", "R1", "L5", "L3", "R2", "L5", "L3", "R5", "R3", "L4", "L2", "R2", "R4", "R4", "L4", "R5", "L1", "L3", "R3", "R4", "R4", "L5", "R4", "R2", "L3", "R4", "R2", "R1", "R2", "L4", "L2", "R2", "L5", "L5", "L3", "R5", "L5", "L1", "R4", "L1", "R1", "L1", "R4", "L5", "L3", "R4", "R1", "L3", "R4", "R1", "L3", "L1", "R1", "R2", "L4", "L2", "R1", "L5", "L4", "L5"]
#print(Day1.solutionPart1(input))
print(Day1.solutionPart2(input))
