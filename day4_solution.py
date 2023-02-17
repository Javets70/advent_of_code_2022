class pairComparison:
    def __init__(self, filePath: str):
        self.rdata = open(filePath).readlines()

    @staticmethod
    def getPair(item: str):
        a, b = item.split(",")
        range1 = list(map(int, a.split("-")))
        range2 = list(map(int, b.split("-")))
        return range1, range2

    @staticmethod
    def checkRangeOverlap(range1: list, range2: list):
        if range2[0] >= range1[0] and range2[-1] <= range1[-1]:
            return True

    def getAns1(self):
        self.count = 0
        for line in self.rdata:
            firstRange, secondRange = self.getPair(line)
            # print(firstRange, secondRange, self.count, end="\n")
            if self.checkRangeOverlap(
                firstRange, secondRange
            ) or self.checkRangeOverlap(secondRange, firstRange):
                self.count += 1
        return self.count

    @staticmethod
    def checkIntersection(range1: list, range2: list):
        set1 = set(range(range1[0], range1[-1] + 1))
        set2 = set(range(range2[0], range2[-1] + 1))
        if set1.intersection(set2):
            return True

    def getAns2(self):
        self.count = 0
        for line in self.rdata:
            range1, range2 = self.getPair(line)
            if self.checkIntersection(range1, range2):
                self.count += 1

        return self.count


# test = pairComparison("./day4_sample_input.txt")
test = pairComparison("day4_input.txt")
# print(test.getAns1())
print(test.getAns2())
