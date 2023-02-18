class winCalc:
    a = {"X": 1, "Y": 2, "Z": 3}
    a2 = {"rock": 1, "paper": 2, "scissor": 3}

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

    @staticmethod
    def requiredMove(elfMove: str, Condition: str):
        if Condition == "X":  # lose
            if elfMove == "A":
                return "scissor"
            elif elfMove == "B":
                return "rock"
            elif elfMove == "C":
                return "paper"
        elif Condition == "Y":  # draw
            if elfMove == "A":
                return "rock"
            elif elfMove == "B":
                return "paper"
            elif elfMove == "C":
                return "scissor"
        else:  # win
            if elfMove == "A":
                return "paper"
            elif elfMove == "B":
                return "scissor"
            else:
                return "rock"

    def getAns2(self):
        self.processData()
        self.score = 0
        for line in self.rdata:
            a, b = line.split()
            self.score += winPoints.points2[self.requiredMove(a, b)]
            if b == "X":  # lose
                continue
            elif b == "Y":
                self.score += 3
                continue
            else:
                self.score += 6
                continue

        return self.score


# winPoints = winCalc("./day2_sample_input.txt")
winPoints = winCalc("./day2_input.txt")
# print(winPoints.getAns1())
print(winPoints.getAns2())
print(winPoints.getAns2())
