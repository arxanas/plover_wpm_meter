import time

from PyQt5.QtCore import Qt, QTimer, pyqtSlot

from plover.gui_qt.tool import Tool
from textstat.textstat import textstat

from plover_wpm_meter.wpm_meter_ui import Ui_WpmMeter

_NUM_SYLLABLES_PER_WORD = 1.44


class PloverWpmMeter(Tool, Ui_WpmMeter):
    TITLE = "WPM Meter"

    _TIMEOUTS = {
        "wpm1": 10,
        "wpm2": 60,
    }

    def __init__(self, engine):
        super().__init__(engine)
        self.setupUi(self)

        self._timer = QTimer()
        self._timer.setInterval(100)
        self._timer.setTimerType(Qt.PreciseTimer)
        self._timer.timeout.connect(self._update_wpms)
        self._timer.start()

        self._chars = []
        engine.signal_connect("translated", self._on_translation)

    def _on_translation(self, old, new):
        for action in old:
            remove = len(action.text)
            if remove > 0:
                self._chars = self._chars[:-remove]
            self._chars += _timestamp_chars(action.replace)

        for action in new:
            remove = len(action.replace)
            if remove > 0:
                self._chars = self._chars[:-remove]
            self._chars += _timestamp_chars(action.text)

        self._update_wpms()

    @pyqtSlot()
    def _update_wpms(self):
        max_timeout = max(self._TIMEOUTS.values())
        self._chars = _filter_old_chars(self._chars, max_timeout)
        for name, timeout in self._TIMEOUTS.items():
            chars = _filter_old_chars(self._chars, timeout)
            wpm = _wpm_of_chars(chars, timeout)
            getattr(self, name).display(str(wpm))


def _timestamp_chars(chars):
    current_time = time.time()
    return [(c, current_time) for c in chars]


def _filter_old_chars(chars, timeout):
    current_time = time.time()
    return [(c, t) for c, t in chars
            if (current_time - t) <= timeout]


def _wpm_of_chars(chars, timeout):
    text = "".join(c for c, _ in chars)
    num_words = textstat.syllable_count(text) / _NUM_SYLLABLES_PER_WORD
    num_minutes = timeout / 60
    num_words_per_minute = num_words / num_minutes
    return int(round(num_words_per_minute))
