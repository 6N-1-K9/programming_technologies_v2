import yaml

from DataReader import DataReader
from Types import DataType


class YamlDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as file:
            data = yaml.safe_load(file)

        students = {}

        for item in data:
            for student, subjects in item.items():
                students[student] = list(subjects.items())

        return students
