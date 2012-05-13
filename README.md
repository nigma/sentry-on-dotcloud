Sentry on DotCloud
==================

[Sentry](https://github.com/dcramer/sentry) is a realtime event logging
and aggregation platform written in Python. It collects error logs including
stack traces and local vars from applications and sends out email notifications.
It also has client libraries for Django, JavaScript, Java and a
[couple more](http://sentry.readthedocs.org/en/latest/client/index.html).

![Sentry](http://media.ig.ma/attach/2012/sentry-on-dotcloud/sentry.png)

[DotCloud](https://www.dotcloud.com/) is a managed application hosting that
provides a wide range of services (web servers, databases, caching, etc.)
and makes it trivial to deploy applications.

This small project helps you to run Sentry and fits in a DotCloud's Free Plan
making it an affordable platform for tracking errors in your applications.


Prerequisites
-------------

First you need to sign up for DotCloud account and
[install their command-line client](http://docs.dotcloud.com/firststeps/install/).
Windows users may be interested in
[DotCloudWin](https://github.com/speier/DotCloudWin/downloads) which does not
require Cygwin installation.


Getting the Code
----------------

Clone the [project repository](https://github.com/nigma/sentry-on-dotcloud) and
cd into the new directory:

    git clone git://github.com/nigma/sentry-on-dotcloud.git
    cd sentry-on-dotcloud


Configuration
-------------

Before you deploy the code it is recommended to make a couple adjustments
in the configuration files.

Set random ``SECRET_KEY`` value in the ``sentry_conf.py`` file. You can use the
included ``generate_secret.py`` script or the following Python snippet
to generate a random key:

    import random
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    print "".join([random.choice(chars) for i in range(50)])


Deployment
----------

Use the DotCloud CLI client to create a new project called ``sentry``
and to push the application and configuration files:

    dotcloud create sentry
    dotcloud push sentry .

The url of the new application instance can be found using:

    dotcloud url sentry

After you log in with the default credentials (``admin``/``password``)
it is strongly recommended to change your admin user password and email.


Other Resources
---------------

- Sentry documentation - [http://sentry.readthedocs.org/en/latest/](http://sentry.readthedocs.org/en/latest/)
- [Similar project](https://github.com/kencochrane/sentry-on-dotcloud)
  by Ken Cochrane. The main difference is that this one uses a recent version 4
  of Sentry, enables background task processing using Celery
  and has a simpler structure.
- GitHub repository - [https://github.com/nigma/sentry-on-dotcloud](https://github.com/nigma/sentry-on-dotcloud)
- Related blog post - [http://en.ig.ma/notebook/2012/sentry-on-dotcloud](http://en.ig.ma/notebook/2012/sentry-on-dotcloud)
