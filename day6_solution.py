class signalFixer:
    def __init__(self, filePath: str) -> None:
        self.rdata = open(filePath).read().replace("\n", "")

    @staticmethod
    def checkCharacters(characters: str):
        for char in characters:
            if characters.count(char) > 1:
                return False
        return True

    def getAns1(self):
        for i in range(len(self.rdata) - 4):
            characters = self.rdata[i : i + 4]
            if self.checkCharacters(characters):
                return i + 4

    def getAns2(self):
        for i in range(len(self.rdata) - 14):
            characters = self.rdata[i : i + 14]
            if self.checkCharacters(characters):
                return i + 14


# s = signalFixer("./day6_sample_input.txt")
s = signalFixer("./day6_input.txt")
print(s.getAns1())
print(s.getAns2())
