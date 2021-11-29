class Fractie:

    numarator = 0
    numitor = 1

    def __init__(self, numarator, numitor):
        if numitor == 0:
            self.numitor = 1
            self.numarator = numarator

        if numarator == numitor:
            self.numarator = 1
            self.numarator = 1

        for n in range(numitor, 0, -1):
            if numitor % n == 0 and numarator % n == 0:
                self.numarator = numarator / n
                self.numitor = numitor / n
                break

    def __str__(self):
        return str(int(self.numarator)) + "\\" + str(int(self.numitor))

    def __add__(self, other):
        numarator = self.numarator * other.numitor + other.numarator * self.numitor
        numitor = self.numitor * other.numitor
        return Fractie(int(numarator), int(numitor))

    def __sub__(self, other):
        numarator = self.numarator * other.numitor - other.numarator * self.numitor
        numitor = self.numitor * other.numitor
        return Fractie(int(numarator), int(numitor))

    def inverse(self):
        return Fractie(int(self.numitor), int(self.numarator))


