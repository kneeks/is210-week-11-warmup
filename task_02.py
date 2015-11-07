#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides functions specifically related to time."""


import time


class Snapshot(object):
    """Object that stores a unix timestamp"""

    def __init__(self):
        """
        Creates a unix timestamp.

        Returns:
            returns the current Unix Timestamp

        Examples:
            >>> mysnap = Snapshot()
            >>> hasattr(mysnap, 'created')
            True
        """
        self.created = time.time()
