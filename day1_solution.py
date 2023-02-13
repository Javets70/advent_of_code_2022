class getCalories:
    def __init__(self, filePath: str) -> None:
        with open(filePath) as file:
            self.rdata = file.readlines()  # rawdata

    def processData(self):
        emptyLineCount = 0
        self.dataDict = {0: []}
        for line in self.rdata:
            if not line.strip().isnumeric():  # remove empty line and check if integer
                emptyLineCount += 1
                self.dataDict[emptyLineCount] = []
            else:
                self.dataDict[emptyLineCount] += [
                    int(line.replace("\n", ""))
                ]  # remove new line and convert to int

    def getAns1(self):
        self.processData()
        return max([sum(value) for value in self.dataDict.values()])

    def getAns2(self):
        return sum(
            sorted([sum(value) for value in self.dataDict.values()], reverse=True)[0:3]
        )


# elfCalories = getCalories("./sample_input.txt")
elfCalories = getCalories("./day1_input.txt")
print(elfCalories.getAns1())
print(elfCalories.getAns2())
