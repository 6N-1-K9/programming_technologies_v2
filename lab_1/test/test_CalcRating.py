from CalcRating import CalcRating


def test_calc():
    students = {
        "Иванов": [("математика", 80), ("физика", 100)],
        "Петров": [("математика", 60), ("физика", 80)],
    }

    rating = CalcRating(students).calc()

    assert rating["Иванов"] == 90
    assert rating["Петров"] == 70
