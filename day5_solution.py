class moveCrates:
    def __init__(self, filePath: str):
        self.rdata = open(filePath).readlines()

    def getCrates(self):
        for idx, elem in enumerate(self.rdata):
            if elem == "\n":
                self.crates = self.rdata[:idx]
                self.commands = self.rdata[idx + 1:]
                break

    def makeCrates(self):
        self.getCrates()
        numberOfStacks = int(
            self.crates[-1].rstrip("\n").split()[-1]
        )  # remove newline , split it , get last char
        self.crateDict = {}
        for i in range(1, numberOfStacks + 1):
            self.crateDict[i] = []  # create empty crateDict

        # Add elements to crateDict
        for _, elem in enumerate(self.crates[:-1]):
            for idx2, elem2 in enumerate(elem):
                if idx2 % 4 == 1 and elem2.isupper():  # check if elem is not space
                    self.crateDict[idx2 // 4 + 1].append(elem2)

        for command in self.commands:
            command = command.split()
            count, _from, to = int(command[1]), int(
                command[3]), int(command[5])
            print(self.crateDict)
            self.moveCrates(self.crateDict, count, _from, to)
            print(self.crateDict, "\n")

        return self.crateDict

    @staticmethod
    def moveCrates(crateDict: dict, count: int, _from: int, to: int):
        cratesToMove = crateDict[_from][:count][
            ::-1
        ]  # remove reverse indexing to get ans1
        crateDict[_from] = crateDict[_from][count:]
        for i in cratesToMove:
            crateDict[to].insert(0, i)
            # crateDict[to].append(i)

    def getAns(self):
        self.makeCrates()
        output_str = ""
        for item in self.crateDict.values():
            output_str += item[0]
        return output_str


# test = moveCrates("./day5_sample_input.txt")
test = moveCrates("./day5_input.txt")
print(test.getAns())
