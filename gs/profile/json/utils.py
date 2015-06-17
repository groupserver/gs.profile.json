# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
#
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from gs.group.member.base import user_member_of_group
from gs.profile.email.base import EmailUser


def email_info(siteInfo, userInfo):
    eu = EmailUser(siteInfo.siteObj, userInfo)
    allEmail = eu.get_addresses()
    preferred = eu.get_delivery_addresses()
    unverified = eu.get_unverified_addresses()
    other = list(set(allEmail) - set(preferred) - set(unverified))

    retval = {'all': allEmail,
              'preferred': preferred,
              'other': other,
              'unverified': unverified, }
    return retval

#: The types of folder that can be a group
FOLDER_TYPES = ['Folder', 'Folder (ordered)']


def groups(siteInfo, userInfo):
    groupsFolder = getattr(siteInfo.siteObj, 'groups')
    groups = [folder for folder in groupsFolder.objectValues(FOLDER_TYPES)
              if folder.getProperty('is_group', False)]
    retval = [group.getId() for group in groups
              if user_member_of_group(userInfo, group)]
    return retval


def user_info(siteInfo, userInfo):
    retval = {'id': userInfo.id,
              'name': userInfo.name,
              'url': ''.join((siteInfo.url, userInfo.url)), }
    return retval
