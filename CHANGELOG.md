# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [1.3.3] - 2021-06-19

### Changed

- Minimized the number of SQL queries to improve performance


## [1.3.2] - 2021-03-15

### Fixed

- Month number for March in time selection


## [1.3.1] - 2021-01-28

### Changed

- Moved `AA_TIMEZONE_DEFAULT_PANELS` into its own constants file, so it can also be
  used by other apps as well.


## [1.3.0] - 2021-01-12

### Removed

- Django 2 support


## [1.2.2] - 2020-12-16

### Fixed

- Bootstap classes in template


## [1.2.1] - 2020-10-09

### Fixed

- Column name in admin view
- Timezones re-added in selector in adjust time mode

### Added

- Summary after time zone import during install

### Changed

- Timestamp is now a real part of the URL instead of a hash added to it. The old
  URLs with the hash are still supported and work as well in case you have links to
  it somewhere ...

### Updated

- German translation


## [1.2.0] - 2020-09-27

### Changed

- Settings moved to database instead of `local.py`


## [1.1.0] - 2020-09-23

### Checked

- Compatibility with the upcoming changes in Alliance Auth v2.8.0 (Django 3)

### Added

- German translation to UI
- Translations for Russian, Spansih, Korean and Chinese prepared, need translators
  though. So if you wanna help out, [feel free to to so here](https://www.transifex.com/ppfeufer/aa-timezones/dashboard/).


## [1.0.0] - 2020-09-13

### Changed

- use moment.js provided by AA. No need to provide our own when AA does that for us.
  If you are concerned about using the coudflare CDN, try using the
  [AA GDPR](https://gitlab.com/soratidus999/aa-gdpr) package


## [0.1.9] - 2020-08-01

### Fixed

- hours, minutes and seconds now have leading 0 when below 10
- when countdown is over it no longer counts into negative

### Changed

- Countdown text "Time left" instead of "Time until"


## [0.1.8] - 2020-06-23

### Added

- Time until in "Set Time" mode (#19)


## [0.1.7] - 2020-06-11

### Changed

- Menu icon updated to FontAwesome v5, which allianceauth uses since 2.7.2


## [0.1.6] - 2020-06-09

### Changed

- Readme updated
- Prepared to be served via Pypi


## [0.1.5] - 2020-05-17

### Added

- Set up your own additional time zone panels via `local.py` (see readme)


## [0.1.4] - 2020-05-16

### Changed

- Button labels to better reflect what they are doing
- Month numbers into names in Adjust Time section
- Adjust time buttons are now a bit larger
- Order of information in the time zone panels


## [0.1.3] - 2020-05-15

### Added

- UTC offset

### Updated

- moment.js and timeago.js to their latest versions


## [0.1.2] - 2020-05-15

### Changed

- TZ panels now have their own template
- Chinese TZ panel now has also Russia / Siberia


## [0.1.1] - 2020-05-14

### Fixed

- Bootstrap template hierarchy


## [0.1.0] - 2020-05-14

### Added

- initial version
