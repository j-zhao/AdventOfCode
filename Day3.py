"""
http://adventofcode.com/2016/day/3
"""

class Day3(object):
    def solutionPart1():
        counter = 0
        with open("inputs/Day3.txt") as inp:
            for line in inp:
                strippedLine = line.strip().split()
                strippedLine = list(map(int, strippedLine))
                if (strippedLine[0] + strippedLine[1] > strippedLine[2]
                        and strippedLine[0] + strippedLine[2] > strippedLine[1]
                        and strippedLine[1] + strippedLine[2] > strippedLine[0]):
                    counter += 1
        return counter

    def solutionPart2():
        counter = 0
        with open("inputs/Day3.txt") as inp:
            rows = []
            for line in inp:
                rows.append(list(map(int,line.strip().split())))
                if len(rows) == 3:
                    tri1 = [rows[0][0], rows[1][0], rows[2][0]]
                    tri2 = [rows[0][1], rows[1][1], rows[2][1]]
                    tri3 = [rows[0][2], rows[1][2], rows[2][2]]
                    if (tri1[0] + tri1[1] > tri1[2]
                            and tri1[1] + tri1[2] > tri1[0]
                            and tri1[0] + tri1[2] > tri1[1]):
                        counter += 1
                    if (tri2[0] + tri2[1] > tri2[2]
                            and tri2[1] + tri2[2] > tri2[0]
                            and tri2[0] + tri2[2] > tri2[1]):
                        counter += 1
                    if (tri3[0] + tri3[1] > tri3[2]
                            and tri3[1] + tri3[2] > tri3[0]
                            and tri3[0] + tri3[2] > tri3[1]):
                        counter += 1
                    rows = []
        return counter

    if __name__ == '__main__':
        print(solutionPart1())
        print(solutionPart2())
