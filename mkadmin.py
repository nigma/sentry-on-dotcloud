#!/usr/bin/env python
#-*- coding: utf-8 -*-

import wsgi # setup env
from django.contrib.auth.models import User

u, created = User.objects.get_or_create(username="admin")
if created:
    u.set_password("password")
    u.email = "mail@example.net"
    u.is_superuser = True
    u.is_staff = True
    u.save()
