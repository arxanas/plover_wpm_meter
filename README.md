# About

This is a plugin for Plover to display your typing speed, in words per minute,
as you type. Words per minute is calculated in one of two ways:

  * **NCRA**: The [National Court Reporters Association](https://www.ncra.org/)
    defines a "word" as 1.4 syllables. This is the measure used for official
    NCRA testing material.
  * **Traditional**: The traditional metric for "word" in the context of
    keyboarding is defined to be 5 characters per word, including spaces.

It looks like this:

![The WPM meter in action](media/wpm-meter.png)

# Installation

To install this plugin, you'll need to build Plover from source, then install
this package with an invocation something like this:

```
pip install git+git://github.com/arxanas/plover_wpm_meter
```

Then launch Plover and select the WPM meter from the tools.

# License

This plugin is licensed under the GPLv3.
