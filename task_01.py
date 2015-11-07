#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""accessing custom class instances"""


import produce


TOMATO = produce.Produce()

EGGPLANT = produce.Produce(1311210802)

TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT_EXPRIRES = EGGPLANT.get_expiration()
