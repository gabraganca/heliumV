heliumV
=========
[![Build Status](https://travis-ci.org/gabraganca/heliumV.svg?branch=master)](https://travis-ci.org/gabraganca/heliumV)
[![Coverage Status](https://coveralls.io/repos/github/gabraganca/heliumV/badge.svg?branch=master)](https://coveralls.io/github/gabraganca/heliumV?branch=master)

This software calculates the projected rotational velocity (*vsini*) of a OB
star using the Full Width at Half Maximum (FWHM) of He I lines at 4026, 4388
and 4471 Angstroms. It is based on the work of [Daflon et al. (2007)][1].

[1]: http://dx.doi.org/10.1086/521707


## Usage

Programmatically, the main part you will want to use is the `MeanVshe` object
that can be imported using:

```
from heliumv import HeV
```

To calculate the *vsini* we should use:

```
HeV(10).get_vsni(17000, 4026, 3)
```

For the case where we had hypothetically calculated a FHWM of 3 angstroms to
the He I line at 4026 angstroms in 10,000 resolution spectrum for a star with
temperature equal to 17000 K.

If you will be using the grid more than one time, it is recommended to load it
first and then proceed with the calculations. By following this approach, it
will not load the grid multiple times.

```
# Load the class and the grid
grid = HeV(10)

# Calculate vsini
vsini1 = grid(17000, 4026, 3)

vsini2 = grid(23000, 4471, 2)
```
