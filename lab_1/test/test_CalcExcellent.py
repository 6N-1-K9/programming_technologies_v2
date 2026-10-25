from CalcExcellent import CalcExcellent


def test_calc():
    students = {
        "Иванов": [("математика", 90), ("физика", 95)],
        "Петров": [("математика", 100), ("физика", 80)],
        "Сидоров": [("математика", 95), ("физика", 100)],
    }

    result = CalcExcellent(students).calc()

    assert result == 2
