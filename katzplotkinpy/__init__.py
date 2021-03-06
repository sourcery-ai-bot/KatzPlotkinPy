#!/usr/bin/env python3

import collections

# from .afgen import X

__VersionInfo = collections.namedtuple("VersionInfo", ("major", "minor", "micro"))

__version__ = "0.0.2"
__version_info__ = __VersionInfo(*(map(int, __version__.split("."))))

del collections, __VersionInfo
