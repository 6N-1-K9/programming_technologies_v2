from pathlib import Path


from YamlDataReader import YamlDataReader


def test_read():
    path = Path(__file__).resolve().parents[1] / "data" / "data.yaml"

    students = YamlDataReader().read(str(path))

    assert len(students) == 3
    assert students["Сидоров Алексей Сергеевич"] == [
        ("математика", 95),
        ("программирование", 92),
        ("физика", 100),
    ]
