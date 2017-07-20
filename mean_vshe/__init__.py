"""
MEAN_VSHE
=========

This software calculates the projected rotational velocity (*vsini*) of a OB
star using the Full Width at Half Maximum (FWHM) of He I lines at 4026, 4388
and 4471 Angstroms. It is absed on the work of [Daflon et al. (2007)][1].

[1]: http://dx.doi.org/10.1086/521707

"""
from .main import MeanVshe
