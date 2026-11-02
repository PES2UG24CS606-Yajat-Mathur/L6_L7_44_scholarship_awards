import pytest

from scholarship_awards import application_status, award_amount, is_eligible


@pytest.mark.parametrize(
    ("category", "marks", "income_level", "is_renewal", "expected"),
    [
        ("merit", 75, "low", False, 0),
        ("merit", 80, "low", False, 500),
        ("merit", 91, "low", False, 2560),
        ("merit", 91, "high", False, 1600),
        ("merit", 70, "low", True, 0),
        ("sports", 76, "high", True, 1600),
    ],
)
def test_award_amount_returns_expected_values(
    category, marks, income_level, is_renewal, expected
):
    assert award_amount(category, marks, income_level, is_renewal) == expected


@pytest.mark.parametrize(
    ("category", "marks", "income_level", "is_renewal", "message"),
    [
        ("science", 90, "low", False, "unknown category"),
        ("merit", -1, "low", False, "invalid marks"),
    ],
)
def test_award_amount_rejects_invalid_values(
    category, marks, income_level, is_renewal, message
):
    with pytest.raises(ValueError, match=message):
        award_amount(category, marks, income_level, is_renewal)


@pytest.mark.parametrize(
    ("attendance", "backlogs", "is_special_quota", "expected"),
    [
        (90, 0, False, True),
        (74, 0, False, False),
        (75, 1, False, True),
        (75, 2, False, False),
        (40, 2, True, True),
        (40, 3, True, False),
    ],
)
def test_is_eligible_returns_expected_values(
    attendance, backlogs, is_special_quota, expected
):
    assert is_eligible(attendance, backlogs, is_special_quota) is expected


@pytest.mark.parametrize(
    ("days_left", "is_renewal", "is_paper", "expected"),
    [
        (20, False, False, "open"),
        (19, False, False, "closing"),
        (4, False, False, "closed"),
        (30, True, False, "open"),
        (29, True, False, "closing"),
        (14, True, False, "closed"),
        (30, False, True, "open"),
        (40, True, True, "open"),
    ],
)
def test_application_status_returns_expected_values(
    days_left, is_renewal, is_paper, expected
):
    assert application_status(days_left, is_renewal, is_paper) == expected
