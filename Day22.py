"""
http://adventofcode.com/2016/day/22
"""

class Day22(object):
    def solutionPart1():
        # nodea.used <= nodeb.avail
        counter = 0
        with open("inputs/Day22.txt") as inp:
            inp.readline()
            inp.readline()
            mat = []
            for line in inp:
                arr = line.strip().split()
                tup = (arr[0], int(arr[1][:-1]), int(arr[2][:-1]),
                        int(arr[3][:-1]), int(arr[4][:-1]))
                mat.append(tup)
            sortAvail = sorted(mat, reverse = 1, key = lambda tup: tup[3])
            sortUsed = sorted(mat, reverse = 1, key = lambda tup: tup[2])
            a = 0
            u = 0
            visited = set(sortAvail[0][0])
            while a < len(sortAvail) and u < len(sortUsed):
                used = sortUsed[u]
                avail = sortAvail[a]
                if avail[3] < used[2]:
                    u += 1
                else:
                    if (used[2] > 0
                        and used[0] != avail[0]):
                        if used[0] not in visited:
                            counter += (len(sortUsed) - u)
                            print("NEW PAIR, COUNTER: " + str(counter))
                            print("USED: " + str(used))
                            print("AVAIL:" + str(avail))
                    a += 1
                    visited.add(avail[0])
            return counter

    if __name__ == '__main__':
        print(solutionPart1())
