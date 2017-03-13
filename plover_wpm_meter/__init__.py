import time

from PyQt5.QtCore import Qt, QTimer, pyqtSlot

from plover.gui_qt.tool import Tool

from plover_wpm_meter.textstat.textstat import textstat
from plover_wpm_meter.wpm_meter_ui import Ui_WpmMeter


class PloverWpmMeter(Tool, Ui_WpmMeter):
    TITLE = "WPM Meter"
    ROLE = "wpm_meter"

    _TIMEOUTS = {
        "wpm1": 10,
        "wpm2": 60,
    }

    def __init__(self, engine):
        super().__init__(engine)
        self.setupUi(self)

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.wpm_method.addItem("NCRA", "ncra")
        self.wpm_method.addItem("Traditional", "traditional")

        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.setTimerType(Qt.PreciseTimer)
        self._timer.timeout.connect(self._update_wpms)
        self._timer.start()

        self._chars = []
        engine.signal_connect("translated", self._on_translation)

        self.restore_state()
        self.finished.connect(self.save_state)

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

    @pyqtSlot()
    def _update_wpms(self):
        max_timeout = max(self._TIMEOUTS.values())
        self._chars = _filter_old_chars(self._chars, max_timeout)
        for name, timeout in self._TIMEOUTS.items():
            chars = _filter_old_chars(self._chars, timeout)
            wpm = _wpm_of_chars(chars, method=self.wpm_method.currentData())
            getattr(self, name).display(str(wpm))


def _timestamp_chars(chars):
    current_time = time.time()
    return [(c, current_time) for c in chars]


def _filter_old_chars(chars, timeout):
    current_time = time.time()
    return [(c, t) for c, t in chars
            if (current_time - t) <= timeout]


def _words_in_text(string, method):
    if method == "ncra":
        # The NCRA defines a "word" to be 1.4 syllables, which is the average
        # number of syllables per English word.
        syllables_per_word = 1.4
        # For some reason, textstat returns syllable counts such as a
        # one-syllable word like "the" being 0.9 syllables.
        syllables_in_text = textstat.syllable_count(string) / 0.9
        return syllables_in_text * (1 / syllables_per_word)
    elif method == "traditional":
        # Formal definition; see https://en.wikipedia.org/wiki/Words_per_minute
        return len(string) / 5
    else:
        assert False, "bad wpm method: " + method


def _wpm_of_chars(chars, method):
    if not chars:
        return 0

    start_time = min(t for _, t in chars)
    current_time = time.time()
    time_interval = current_time - start_time
    time_interval = max(1, time_interval)

    text = "".join(c for c, _ in chars)
    num_words = _words_in_text(text, method)
    num_minutes = time_interval / 60
    num_words_per_minute = num_words / num_minutes
    return int(round(num_words_per_minute))
