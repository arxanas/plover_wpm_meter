import mock

from plover_wpm_meter import _timestamp_chars, _filter_old_chars, _wpm_of_chars


@mock.patch("time.time")
def test_timestamp_chars(time):
    time.return_value = 1
    assert _timestamp_chars("foo") == [("f", 1), ("o", 1), ("o", 1)]


@mock.patch("time.time")
def test_filter_old_chars(time):
    time.return_value = 20
    chars = [("a", 0), ("b", 10), ("c", 20)]
    assert _filter_old_chars(chars, 10) == [("b", 10), ("c", 20)]


def test_wpm_of_nothing():
    assert _wpm_of_chars(_timestamp_chars("")) == 0


@mock.patch("time.time")
def test_wpm_of_chars(time):
    time.return_value = 10
    chars = [("f", 5), ("o", 5), ("o", 5), ("o", 5), ("o", 5)]
    assert _wpm_of_chars(chars) == 12


def test_wpm_when_starting_up():
    assert _wpm_of_chars(_timestamp_chars("foooo barr")) == 120
