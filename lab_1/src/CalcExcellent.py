from Types import DataType


class CalcExcellent:

    def __init__(self, data: DataType):
        self.data = data

    def calc(self) -> int:
        count = 0

        for subjects in self.data.values():
            if subjects and all(score >= 90 for _, score in subjects):
                count += 1

        return count
