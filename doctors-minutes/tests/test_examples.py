from datetime import datetime

from doctorsMinutes import calculate_doctors_minutes


def _test_doctors_minutes(start, finish, expectedPremium, expectedNonPremium):
    calculatedMinutes = calculate_doctors_minutes(start, finish)

    print("input dates:", start, finish)
    print("output minutes:", calculatedMinutes.premium, calculatedMinutes.nonPremium)
    print("expected minutes", expectedPremium, expectedNonPremium)

    assert expectedPremium == calculatedMinutes.premium
    assert expectedNonPremium == calculatedMinutes.nonPremium


def test_example_1():
    start = datetime(2016, 3, 21, 6)
    finish = datetime(2016, 3, 21, 10)

    _test_doctors_minutes(start, finish, 60, 180)


def test_example_2():
    start = datetime(2016, 3, 25, 0)
    finish = datetime(2016, 3, 25, 12)

    _test_doctors_minutes(start, finish, 7 * 60, 5 * 60)


def test_example_3():
    start = datetime(2016, 3, 26, 0)
    finish = datetime(2016, 3, 26, 12)

    _test_doctors_minutes(start, finish, 12 * 60, 0)
