from hypothesis import given, settings, strategies as st
from scholarship_awards import parse_applicant, marks_average, payable_award

@given(st.text() | st.none())
@settings(deadline=None)
def test_parse_applicant_no_crash(s):
    parse_applicant(s)

@given(st.text() | st.none())
@settings(deadline=None)
def test_marks_average_no_crash(s):
    marks_average(s)

@given(st.text() | st.none())
@settings(deadline=None)
def test_payable_award_no_crash(s):
    payable_award(s)


def test_valid_inputs_keep_existing_results():
    assert parse_applicant("merit:82") == ("Merit", 82.0)
    assert marks_average("72,85,90") == 82
    assert payable_award("5000|500") == 5400.0


def test_invalid_inputs_are_rejected():
    assert parse_applicant(None) is None
    assert parse_applicant(":82") is None
    assert parse_applicant("merit:not-a-number") is None
    assert marks_average(None) is None
    assert marks_average("72,,90") is None
    assert payable_award(None) is None
    assert payable_award("500|") is None
    assert payable_award("1.7e308|0") is None
