from DataReader import DataReader
from Types import DataType


class TextDataReader(DataReader):

    def read(self, path: str) -> DataType:
        students = {}

        with open(path, encoding="utf-8") as file:
            for line in file:
                if not line.startswith(" "):
                    student = line.strip()
                    students[student] = []
                else:
                    subject, score = line.split(":")
                    students[student].append(
                        (subject.strip(), int(score.strip()))
                    )

        return students
