#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing an existing class"""


import produce


class Apple(produce.Produce):
    """
    Subclassed from produce.

    Attributes:
        duration(int): any value
    """

    duration = 5356800
