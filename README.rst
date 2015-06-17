===================
``gs.profile.json``
===================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A JSON view of the GroupServer profile of a person
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-01-30
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

This product provides a view of a profile of a GroupServer_ group
member in JSON_ format. It is used by the `member export`_
system, and requires the person retrieving the information to be
logged in.

Member export
=============

The JSON view of the profile, ``profile.json`` in the *profile*
context, returns the profile information to people who are logged
in. It is used by the ``gs.group.member.export`` system to
produce a CSV of profile information for the group members.

Resources
=========

- Code repository: https://github.com/groupserver/gs.profile.json
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

..  LocalWords:  nz GSProfile TODO redirector LocalWords JSON json CSV
