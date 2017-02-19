import mock

from plover_wpm_meter import (
    _NUM_SYLLABLES_PER_WORD,
    _timestamp_chars,
    _filter_old_chars,
    _wpm_of_chars,
)


@mock.patch("time.time")
def test_timestamp_chars(time):
    time.return_value = 1
    assert _timestamp_chars("foo") == [("f", 1), ("o", 1), ("o", 1)]


@mock.patch("time.time")
def test_filter_old_chars(time):
    time.return_value = 20
    chars = [("a", 0), ("b", 10), ("c", 20)]
    assert _filter_old_chars(chars, 10) == [("b", 10), ("c", 20)]


@mock.patch("plover_wpm_meter.textstat")
def test_wpm_of_chars(textstat):
    textstat.syllable_count.return_value = _NUM_SYLLABLES_PER_WORD * 10
    assert _wpm_of_chars(_timestamp_chars("foo"), timeout=10) == 60
