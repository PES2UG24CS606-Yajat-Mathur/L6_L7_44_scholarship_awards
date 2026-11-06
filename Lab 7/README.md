# L6_L7_44 — Scholarship Awards

Lab 7: Fuzz Testing

## About

A small Python module that parses applicant records, averages marks and works out the payable award after a deduction.

## Files

| File | Description |
|------|-------------|
| `scholarship_awards.py` | The code under test |
| `test_scholarship_awards.py` | Hypothesis fuzz and regression tests |
| `Lab_7_FuzzTesting_Evidence.pdf` | Deliverable PDF with output evidence for all four lab stages |

Refer to the lab handout for instructions.

## Run

Install the test dependencies and run the Hypothesis fuzz tests:

```powershell
python -m pip install hypothesis pytest
python -m pytest test_scholarship_awards.py -q
```

The parsing functions return `None` for malformed or non-string input. Valid input retains the original calculations.

## Deliverables

- `PES2UG24CS606_Lab_7_FuzzTesting_Evidence.pdf` — original application output, failing pre-fix fuzz tests, fixed application output, and passing post-fix tests.
- `scholarship_awards.py` — fixed application.
- `test_scholarship_awards.py` — updated Hypothesis tests.
