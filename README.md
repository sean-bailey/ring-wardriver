=====================
Python Wardriver Project
=====================

_"Look ma! I'm a security researcher now!"_

This is essentially a fork of the python-ring-doorbell project by @tchellomello ( https://github.com/tchellomello/python-ring-doorbell ),
however it isn't necessarily a "feature" which needs to be added to that repository, more of a demonstration of
the recent security "vulnerability" Ring has disclosed in the past days. However, I will keep the license from that
code, and can not have come close to doing this demonstration without the incredible work done by @tchellomello to create the python-ring-doorbell library.

Ring recently confirmed that there have been a series of attacks made against it,
and also confirmed that these attacks did not exploit any true security vulnerabilities,
but realistically were done by """hackers""" who acquired the username and password of the
ring doorbell user, and then plugging them in to Ring's endpoint. They acknowledged this,
and, running on AWS, assumedly already have things such as WAF, Guard Duty, and other 3rd party
tools designed to shield against an individual attacker trying to just brute force and randomly guess
the credentials of any user from a long list.

However, as my tool demonstrates, these countermeasures can be reasonably worked around by making your
attack pattern relatively unpredictable (cycling proxies, adding random intervals between attempts, etc).
I'm sure the Ring security team already realizes this and that's why they now are _heavily_ encouraging all
users to enable MFA. I decided to release this tool in order to demonstrate to the layman how simple it is
to attack Ring and _why_ the average user should bite the bullet and enable MFA as Ring suggests.

Installation
------------

Download the repository, cd in to the repo directory and run:

.. code-block:: bash

    # Installing from github repo
    $ python setup.py install


Demonstrating the brute force login attack which Ring is vulnerable against without MFA:
----------------------------------------------------------------------------------------

First, you'll need a set of text files (ending with .txt) somewhere on your system
with the credentials listed line by line as follows:

`user1@email.com:password2`
`user2@email.com:password2`

etc.

Once that's done, run the `ring_wardriver_example.py` inside the `./ring_wardriver/`
directory inside this repo.


This Readme will not go in to the details on the non-security demonstration sections of code,
instead if you'd like to know how the backends of this fantastic tool (seriously) head over to
@tchellomello 's python-ring-doorbell library https://github.com/tchellomello/python-ring-doorbell

How to Integrate the Vulnerability Testing in to your own code:
---------------------------------------------------------------
.. code-block:: python

    from ring_wardriver import Ring
    ringclient = Ring(username=ringuser, password=ringpass, select_proxy=True)
        if ringclient.is_connected:
            print("Got one!")
            print(ringuser + " , " + ringpass)
            print(ringclient.devices)

The `select_proxy` attribute is the real magic here, where it automatically selects a
new workable proxy to then route the request to Ring to and from.



How to contribute
-----------------
This really was a pet project for me, I don't plan on actively maintaining a proof-of-concept.
Run with this as you will, I'll happily take a look at pull requests or bugs raised, but won't take
things too seriously.

I heavily recommend instead of contributing to this repo instead contributing to its parent: https://github.com/tchellomello/python-ring-doorbell


Credits && Thanks
-----------------

* Full accolades to @tchellomello for their python-ring-doorbell library ( https://github.com/tchellomello/python-ring-doorbell ) which this is essentially a fork of, however the purposes of this particular experiment did not constitute a "feature" to be added to that library.
