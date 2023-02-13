class winCalc:
    points = {"X": 1, "Y": 2, "Z": 3}

    def __init__(self, filePath: str) -> None:
        self.filePath = filePath

    def processData(self):
        self.rdata = open(self.filePath).readlines()  # raw data

    def getAns1(self):
        self.processData()
        self.score = 0
        for line in self.rdata:
            a, b = line.split()
            self.score += winCalc.points[b]

            # Rock Conditions
            if a == "A" and b == "Z":  # loss
                continue
            elif a == "A" and b == "X":  # draw
                self.score += 3
                continue
            elif a == "A" and b == "Y":  # win
                self.score += 6
                continue
            # Paper conditions
            elif a == "B" and b == "X":  # loss
                continue
            elif a == "B" and b == "Y":  # draw
                self.score += 3
                continue
            elif a == "B" and b == "Z":  # win
                self.score += 6
                continue
            # Rock Conditions
            elif a == "C" and b == "Y":  # loss
                continue
            elif a == "C" and b == "Z":  # draw
                self.score += 3
                continue
            else:  # win
                self.score += 6
                continue

        return self.score


# winPoints = winCalc("./day2_sample_input.txt")
winPoints = winCalc("./day2_input.txt")
print(winPoints.getAns1())
