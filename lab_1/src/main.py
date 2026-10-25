import argparse

from CalcRating import CalcRating
from CalcExcellent import CalcExcellent
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", required=True)
    args = parser.parse_args()

    if args.p.endswith((".yaml", ".yml")):
        reader = YamlDataReader()
    else:
        reader = TextDataReader()

    students = reader.read(args.p)

    rating = CalcRating(students).calc()
    excellent = CalcExcellent(students).calc()

    print("Средний рейтинг:", rating)
    print("Количество отличников:", excellent)


if __name__ == "__main__":
    main()
