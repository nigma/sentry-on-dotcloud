#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
print "".join([random.choice(chars) for i in range(50)])
