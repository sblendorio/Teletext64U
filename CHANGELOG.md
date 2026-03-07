# **Teletext64U** changelog

## [1.0.2] - 2026-03-07

### Added
Users reporting a black teletext screen at startup now have more information about what could be the problem:
- _Ultimate Command Interface_ detection added at startup; when not detected, the program instructs the user how to enable it.
- PetsciiProxy detection at startup.
- RunMeFirst.cfg. This config file enables the Command Interface and sets the CPU speed to 40Mhz. It's in the Teletext64U/target folder next to the .d64 image. 


## [1.0.1] - 2026-03-05

### Fixed
- Auto refresh timer was off by 3 seconds when running on 1Mhz, because of the time needed to display the teletext page. It now resets before displaying the page.


## [1.0.0] - 2026-03-04
- Initial release of Teletext64U.

### Purpose
- Get it tested by users on various Ultimate products with networking capabilities.