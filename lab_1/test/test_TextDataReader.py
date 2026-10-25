from pathlib import Path


from TextDataReader import TextDataReader


def test_read():
    path = Path(__file__).resolve().parents[1] / "data" / "data.txt"

    students = TextDataReader().read(str(path))

    assert len(students) == 2
    assert students["Иванов Иван Иванович"] == [
        ("математика", 80),
        ("программирование", 90),
        ("литература", 76),
    ]
