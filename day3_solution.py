class getPriority:
    def __init__(self, filePath: str):
        self.rdata = open(filePath).readlines()

    @staticmethod
    def getPriority(common_item):
        common_item = str(common_item).lstrip("{'").rstrip("'}")
        if common_item.isupper():
            return ord(common_item.lower()) + 26 - 96
        else:
            return ord(common_item) - 96

    def getAns1(self):
        self.score = 0
        for line in self.rdata:
            line = line.strip(" ").replace("\n", "")
            middle = int(len(line) / 2)
            first, second = set(line[:middle]), set(line[middle:])
            self.score += self.getPriority(first.intersection(second))

        return self.score

    def getAns2(self):
        self.score = 0
        for i in range(3, len(self.rdata) + 1, 3):
            a, b, c = map(set, self.rdata[i - 3 : i])
            badge = a.intersection(b).intersection(c)
            badge.remove("\n")
            self.score += self.getPriority(badge)

        return self.score


test = getPriority("./day3_input.txt")
# print(test.getAns1())
print(test.getAns2())
