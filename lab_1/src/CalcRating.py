from Types import DataType


class CalcRating:

    def __init__(self, data: DataType):
        self.data = data

    def calc(self) -> dict[str, float]:
        rating = {}

        for student, subjects in self.data.items():
            total = sum(score for _, score in subjects)
            rating[student] = total / len(subjects)

        return rating
