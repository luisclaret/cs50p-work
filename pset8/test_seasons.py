from datetime import date

import pytest

import seasons

from seasons import return_birth_date, string_minutes


class _FixedDate(date):
    @classmethod
    def today(cls):
        return date(2000, 1, 1)


def test_return_birth_date_valid():
    assert return_birth_date("1999-01-01") == date(1999, 1, 1)
    assert return_birth_date("2000-02-29") == date(2000, 2, 29)


def test_return_birth_date_invalid():
    for value in ["January 1, 1999", "1999/01/01", "1999-13-01", "1999-02-30", "99-01-01", ""]:
        with pytest.raises(SystemExit):
            return_birth_date(value)


def test_string_minutes_basic(monkeypatch):
    monkeypatch.setattr(seasons, "date", _FixedDate)
    assert string_minutes("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"


def test_string_minutes_zero(monkeypatch):
    monkeypatch.setattr(seasons, "date", _FixedDate)
    assert string_minutes("2000-01-01") == "Zero minutes"


def test_string_minutes_future(monkeypatch):
    monkeypatch.setattr(seasons, "date", _FixedDate)
    with pytest.raises(SystemExit):
        string_minutes("2001-01-01")


def test_string_minutes_invalid(monkeypatch):
    monkeypatch.setattr(seasons, "date", _FixedDate)
    with pytest.raises(SystemExit):
        string_minutes("not-a-date")
